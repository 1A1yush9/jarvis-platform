"""
Stage-36.0 — Adaptive Operational Learning Loop

Learns from shadow simulations.
Advisory cognition ONLY.
"""

from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass
class AdaptiveLearningState:
    learning_cycle: int
    rolling_performance: float
    learning_stability_index: float
    regression_detected: bool
    adaptive_confidence: float
    execution_allowed: bool = False


class AdaptiveOperationalLearning:

    def __init__(self):
        self.cycle_count = 0
        self.performance_history: List[float] = []
        self.adaptive_confidence = 0.5

    # ----------------------------------
    # Learning Update
    # ----------------------------------
    def update(self, shadow_result: Dict) -> AdaptiveLearningState:

        self.cycle_count += 1

        predicted_score = shadow_result.get("predicted_outcome_score", 0.0)
        simulation_state = shadow_result.get("simulation_state", "UNSTABLE")

        self.performance_history.append(predicted_score)

        # Keep rolling window stable
        if len(self.performance_history) > 20:
            self.performance_history.pop(0)

        rolling_performance = (
            sum(self.performance_history) / len(self.performance_history)
        )

        # Stability index (variance control)
        if len(self.performance_history) > 1:
            variance = max(self.performance_history) - min(self.performance_history)
        else:
            variance = 0.0

        learning_stability_index = max(0.0, 1 - variance)

        regression_detected = predicted_score < (rolling_performance * 0.9)

        # Confidence adaptation
        if simulation_state == "STABLE" and not regression_detected:
            self.adaptive_confidence = min(
                1.0, self.adaptive_confidence + 0.03
            )
        elif regression_detected:
            self.adaptive_confidence = max(
                0.0, self.adaptive_confidence - 0.05
            )

        return AdaptiveLearningState(
            learning_cycle=self.cycle_count,
            rolling_performance=round(rolling_performance, 4),
            learning_stability_index=round(learning_stability_index, 4),
            regression_detected=regression_detected,
            adaptive_confidence=round(self.adaptive_confidence, 4),
            execution_allowed=False,
        )

    # ----------------------------------
    def export(self, shadow_result: Dict) -> Dict:
        return asdict(self.update(shadow_result))