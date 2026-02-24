# =====================================================
# Creative Intelligence Brain
# Learns and ranks marketing creatives automatically
# =====================================================

from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from datetime import datetime
from app.core.database import Base


class CreativeInsight(Base):
    __tablename__ = "creative_insights"

    id = Column(Integer, primary_key=True, index=True)

    industry = Column(String, index=True)
    hook_type = Column(String)
    headline = Column(Text)
    offer_type = Column(String)

    performance_score = Column(Float, default=0.5)

    usage_count = Column(Integer, default=0)
    last_roi = Column(Float, default=0.0)

    created_at = Column(DateTime, default=datetime.utcnow)

class CreativeBrain:

    # -------------------------------------------------
    # Detect psychological hook type
    # -------------------------------------------------
    @staticmethod
    def detect_hook(text: str):

        text_lower = text.lower()

        if "free" in text_lower:
            return "free_offer"

        if "limited" in text_lower or "today" in text_lower:
            return "urgency"

        if "secret" in text_lower or "discover" in text_lower:
            return "curiosity"

        if "save" in text_lower or "discount" in text_lower:
            return "discount"

        return "general"

    # -------------------------------------------------
    # Extract headline-like lines
    # -------------------------------------------------
    @staticmethod
    def extract_headlines(text: str):

        lines = text.split("\n")

        headlines = []
        for line in lines:
            clean = line.strip()

            if len(clean) > 15:
                headlines.append(clean)

        return headlines[:5]

    # -------------------------------------------------
    # Learn creatives from generated campaign
    # -------------------------------------------------
    @staticmethod
    def learn_from_campaign(db, industry: str, generated_text: str):

        headlines = CreativeBrain.extract_headlines(generated_text)

        for headline in headlines:

            # ✅ Prevent duplicate storage
            existing = (
                db.query(CreativeInsight)
                .filter(
                    CreativeInsight.industry == industry,
                    CreativeInsight.headline == headline
                )
                .first()
            )

            if existing:
                continue

            insight = CreativeInsight(
                industry=industry,
                hook_type=CreativeBrain.detect_hook(headline),
                headline=headline,
                offer_type="standard",
                performance_score=0.5,
                usage_count=0,
                last_roi=0.0
            )

            db.add(insight)

        db.commit()

    # -------------------------------------------------
    # Retrieve best creatives
    # -------------------------------------------------
    @staticmethod
    def get_best_creatives(db, industry: str):

        records = (
            db.query(CreativeInsight)
            .filter(CreativeInsight.industry == industry)
            .order_by(CreativeInsight.performance_score.desc())
            .limit(5)
            .all()
        )

        return [r.headline for r in records]

    # -------------------------------------------------
    # Update creative performance using ROI
    # -------------------------------------------------
    @staticmethod
    def update_creative_performance(db, industry: str, roi_score: float):

        records = (
            db.query(CreativeInsight)
            .filter(CreativeInsight.industry == industry)
            .all()
        )

        if not records:
            return

        for r in records:
            r.usage_count += 1
            r.last_roi = roi_score

            r.performance_score = (
                r.performance_score * 0.7 +
                roi_score * 0.3
            )

        db.commit()
