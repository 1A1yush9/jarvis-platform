class RiskEngine:

    def calculate_risk(self, goal):

        risk = 0.0

        # Low confidence = higher risk
        risk += (1 - goal.confidence)

        # Critical priority slightly increases risk
        if goal.priority.value == "critical":
            risk += 0.2

        return min(risk, 1.0)


risk_engine = RiskEngine()
