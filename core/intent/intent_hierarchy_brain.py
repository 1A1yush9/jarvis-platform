from .intent_classifier import intent_classifier


class IntentHierarchyBrain:
    """
    Assigns strategic context to autonomous goals.
    """

    def attach_intent(self, goal):

        intent = intent_classifier.classify_goal(goal)

        # attach intent reference safely
        goal.metadata = goal.metadata or {}
        goal.metadata["intent_id"] = intent.id
        goal.metadata["intent_level"] = intent.level.value

        print(
            f"[Intent] Goal mapped to {intent.level.value}"
        )

        return goal


intent_hierarchy_brain = IntentHierarchyBrain()
