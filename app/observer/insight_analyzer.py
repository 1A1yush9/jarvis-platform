def analyze_state(state: dict):
    insights = []

    if state["cpu_percent"] > 80:
        insights.append("High CPU usage detected")

    if state["memory_percent"] > 80:
        insights.append("Memory pressure rising")

    if not insights:
        insights.append("System stable")

    return {
        "summary": insights,
        "risk_level": "low" if len(insights) == 1 else "medium"
    }