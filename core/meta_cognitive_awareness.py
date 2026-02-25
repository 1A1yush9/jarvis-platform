# core/meta_cognitive_awareness.py

"""
Stage-14.6 — Meta-Cognitive Awareness

Purpose:
Observes Jarvis reasoning quality and produces
self-awareness diagnostics before kernel evaluation.

This layer DOES NOT execute actions.
Advisory cognition only.
"""

from typing import Dict, Any, List


class MetaCognitiveAwareness:

    def __init__(self):
        self.version = "14.6"
        self.mode = "advisory"

    # --------------------------------------------------
    # Confidence Evaluation
    # --------------------------------------------------
    def evaluate_confidence(
        self,
        signals: Dict[str, Any],
        context: Dict[str, Any],
        prediction: Dict[str, Any],
        priority: Dict[str, Any],
    ) -> float:

        score = 0.0
        checks = 4

        if signals:
            score += 1
        if context:
            score += 1
        if prediction:
            score += 1
        if priority:
            score += 1

        return round(score / checks, 2)

    # --------------------------------------------------
    # Risk Detection
    # --------------------------------------------------
    def detect_risks(
        self,
        signals: Dict[str, Any],
        prediction: Dict[str, Any],
        priority: Dict[str, Any],
    ) -> List[str]:

        risks = []

        if not signals:
            risks.append("LOW_SIGNAL_INPUT")

        if prediction.get("uncertainty", 0) > 0.6:
            risks.append("HIGH_PREDICTION_UNCERTAINTY")

        if priority.get("conflict", False):
            risks.append("PRIORITY_CONFLICT")

        return risks

    # --------------------------------------------------
    # Awareness Report
    # --------------------------------------------------
    def generate_awareness(
        self,
        signals: Dict[str, Any],
        context: Dict[str, Any],
        prediction: Dict[str, Any],
        priority: Dict[str, Any],
    ) -> Dict[str, Any]:

        confidence = self.evaluate_confidence(
            signals, context, prediction, priority
        )

        risks = self.detect_risks(signals, prediction, priority)

        if confidence >= 0.75:
            advisory_strength = "STRATEGIC"
        elif confidence >= 0.5:
            advisory_strength = "TACTICAL"
        else:
            advisory_strength = "EXPLORATORY"

        return {
            "stage": "14.6",
            "confidence_score": confidence,
            "risk_flags": risks,
            "reasoning_quality": "stable" if confidence > 0.6 else "uncertain",
            "uncertainty_level": prediction.get("uncertainty", 0),
            "advisory_strength": advisory_strength,
            "adjustment_recommendation":
                "increase signal intake" if confidence < 0.5 else "none",
        }