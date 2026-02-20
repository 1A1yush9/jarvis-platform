from sqlalchemy.orm import Session
from app.core.roi_models import CampaignROI


class StrategyBrain:

    @staticmethod
    def get_best_strategy(db: Session, business_type: str):

        records = db.query(CampaignROI)\
            .filter(CampaignROI.business_type == business_type)\
            .all()

        # No history yet
        if not records:
            return {
                "channels": ["Meta Ads", "Google Ads"],
                "budget_split": {"Meta Ads": 50, "Google Ads": 50},
                "confidence": "low"
            }

        # Calculate averages
        total_roi = sum(r.roi_score for r in records)
        avg_roi = total_roi / len(records)

        # Simple adaptive logic
        if avg_roi > 1.5:
            return {
                "channels": ["Meta Ads", "Google Ads", "SEO"],
                "budget_split": {
                    "Meta Ads": 40,
                    "Google Ads": 40,
                    "SEO": 20
                },
                "confidence": "high"
            }

        elif avg_roi > 0.5:
            return {
                "channels": ["Meta Ads", "Google Ads"],
                "budget_split": {
                    "Meta Ads": 60,
                    "Google Ads": 40
                },
                "confidence": "medium"
            }

        else:
            return {
                "channels": ["Google Ads"],
                "budget_split": {"Google Ads": 100},
                "confidence": "recovery_mode"
            }
