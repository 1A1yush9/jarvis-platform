from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from datetime import datetime
from app.core.database import Base


class CampaignMemory(Base):
    __tablename__ = "campaign_memory"

    id = Column(Integer, primary_key=True, index=True)

    business_type = Column(String, index=True)
    niche = Column(String, index=True)

    client_name = Column(String)
    location = Column(String)

    campaign_input = Column(Text)
    generated_strategy = Column(Text)

    channels_used = Column(String)
    estimated_budget = Column(Float)

    performance_score = Column(Float, default=0.0)

    created_at = Column(DateTime, default=datetime.utcnow)
