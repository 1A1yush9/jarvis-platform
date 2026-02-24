from sqlalchemy.orm import Session
from app.core.roi_models import CampaignROI


class PredictiveBrain:

    @staticmethod
    def predict_campaign(db: Session, business_type: str):

        records = db.query(CampaignROI)\
            .filter(CampaignROI.business_type == business_type)\
            .all()

        # No historical data
        if not records:
            return {
                "predicted_leads": 15,
                "predicted_conversions": 2,
                "predicted_roi": 0.5,
                "risk_level": "high"
            }

        total_leads = sum(r.leads_generated for r in records)
        total_conversions = sum(r.conversions for r in records)
        total_roi = sum(r.roi_score for r in records)

        count = len(records)

        avg_leads = total_leads / count
        avg_conversions = total_conversions / count
        avg_roi = total_roi / count

        # Risk classification
        if avg_roi > 1.5:
            risk = "low"
        elif avg_roi > 0.7:
            risk = "medium"
        else:
            risk = "high"

        return {
            "predicted_leads": round(avg_leads),
            "predicted_conversions": round(avg_conversions),
            "predicted_roi": round(avg_roi, 2),
            "risk_level": risk
        }
