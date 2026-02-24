# ==========================================================
# JARVIS AI — SELF SCALING CLIENT ENGINE
# Stage 11.3
# ==========================================================

from datetime import datetime


class SelfScalingEngine:
    """
    Expands client delivery intelligently based on system capacity.
    """

    def __init__(self):
        self.scaling_log = []
        self.active_projects = 0
        self.capacity_limit = 10  # safe default

    # ------------------------------------------------------
    # Register Active Project
    # ------------------------------------------------------
    def register_project(self):
        self.active_projects += 1

    # ------------------------------------------------------
    # Complete Project
    # ------------------------------------------------------
    def complete_project(self):
        if self.active_projects > 0:
            self.active_projects -= 1

    # ------------------------------------------------------
    # Evaluate Scaling Opportunity
    # ------------------------------------------------------
    def evaluate_scaling(self):

        available_capacity = self.capacity_limit - self.active_projects

        decision = {
            "timestamp": datetime.utcnow(),
            "active_projects": self.active_projects,
            "available_capacity": available_capacity,
            "scale_recommended": available_capacity > 2
        }

        self.scaling_log.append(decision)

        return decision

    # ------------------------------------------------------
    # Recommend Client Expansion
    # ------------------------------------------------------
    def recommend_expansion(self):

        decision = self.evaluate_scaling()

        if decision["scale_recommended"]:
            return {
                "action": "acquire_new_clients",
                "recommended_slots": decision["available_capacity"]
            }

        return {
            "action": "hold_capacity",
            "recommended_slots": 0
        }