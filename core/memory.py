# =====================================================
# Memory System
# Short-term + Long-term Learning
# =====================================================

from app.core.memory_models import CampaignMemory
from app.core.industry_brain import IndustryBrain


# -----------------------------------------------------
# Short-term runtime memory
# -----------------------------------------------------
class MemoryStore:
    """
    Temporary memory during server runtime.
    """

    def __init__(self):
        self.history = []

    def save(self, record: dict):
        self.history.append(record)

    def all(self):
        return self.history


# -----------------------------------------------------
# Long-term AI learning memory
# -----------------------------------------------------
class MemoryBrain:

    # ---------------------------------------------
    # Store campaign learning
    # ---------------------------------------------
    @staticmethod
    def store_campaign(db, data: dict):

        record = CampaignMemory(
            business_type=data["business_type"],
            niche=data["niche"],
            client_name=data["client_name"],
            location=data["location"],
            campaign_input=data["campaign_input"],
            generated_strategy=data["generated_strategy"],
            channels_used=data["channels_used"],
            estimated_budget=data["estimated_budget"],
            performance_score=data["performance_score"]
        )

        db.add(record)
        db.commit()
        db.refresh(record)

        return record

    # ---------------------------------------------
    # Find similar campaigns (Industry Intelligence)
    # ---------------------------------------------
    @staticmethod
    def find_similar(db, business_type: str):

        related_industries = IndustryBrain.get_related_industries(
            business_type
        )

        records = db.query(CampaignMemory).all()

        similar = []

        for r in records:
            if r.business_type.lower() in [
                i.lower() for i in related_industries
            ]:
                similar.append(r)

        similar.sort(
            key=lambda x: x.performance_score,
            reverse=True
        )

        return similar[:5]
