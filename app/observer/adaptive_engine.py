# app/observer/adaptive_engine.py

from app.observer.activity_observer import observer


class AdaptiveEngine:
    """
    Stage-4.5 Adaptive Intelligence
    Generates safe recommendations based on observed behavior.
    """

    def generate_recommendations(self):

        summary = observer.system_summary()
        recommendations = []

        usage = summary.get("most_used_actions", [])

        if not usage:
            return {
                "adaptive_active": True,
                "recommendations": ["Not enough activity yet."]
            }

        top_action, count = usage[0]

        # Pattern rules (safe logic layer)
        if count >= 5 and top_action == "analyze":
            recommendations.append(
                "High analysis usage detected. Consider enabling automated workflows."
            )

        if count >= 10:
            recommendations.append(
                "System heavily used. Scaling or caching layer may be beneficial."
            )

        if not recommendations:
            recommendations.append("System operating normally.")

        return {
            "adaptive_active": True,
            "recommendations": recommendations,
        }


adaptive_engine = AdaptiveEngine()