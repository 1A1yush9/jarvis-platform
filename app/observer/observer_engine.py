from .state_collector import collect_system_state
from .insight_analyzer import analyze_state


class ObserverBrain:

    def observe(self):
        state = collect_system_state()
        analysis = analyze_state(state)

        return {
            "state": state,
            "analysis": analysis,
            "mode": "observer_passive"
        }


observer_brain = ObserverBrain()