from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base


class CampaignROI(Base):
    __tablename__ = "campaign_roi"

    id = Column(Integer, primary_key=True, index=True)

    business_type = Column(String, index=True)

    leads_generated = Column(Integer, default=0)
    conversions = Column(Integer, default=0)

    ad_spend = Column(Float, default=0.0)
    revenue = Column(Float, default=0.0)

    roi_score = Column(Float, default=0.0)

    created_at = Column(DateTime, default=datetime.utcnow)
