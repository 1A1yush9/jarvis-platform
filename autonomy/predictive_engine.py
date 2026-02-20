from .prediction_models import PredictedSignal
from .trend_analyzer import trend_analyzer
from app.core.autonomy.autonomous_goal_engine import autonomous_goal_engine


class PredictiveEngine:

    def analyze_metrics(self, metric_history):

        trend = trend_analyzer.detect_trend(metric_history)

        if trend == "declining":

            signal = PredictedSignal(
                type="performance_drop",
                score=0.75,
                reason="Detected declining performance trend"
            )

            print("[Predictive] Preventive signal generated")

            # Feed into existing pipeline (NON-BREAKING)
            autonomous_goal_engine.process_observer_signal(
                signal.dict()
            )


predictive_engine = PredictiveEngine()
