from app.schemas.task import Task


class TaskGraphBuilder:
    """
    Builds a directed task graph based on the objective.
    """

    def build(self):
        return [
            Task(id="T1", name="Market Scan"),
            Task(id="T2", name="Lead Discovery", depends_on=["T1"]),
            Task(id="T3", name="Lead Validation", depends_on=["T2"]),
            Task(id="T4", name="Opportunity Analysis", depends_on=["T3"]),
            Task(id="T5", name="Outreach Strategy", depends_on=["T4"]),
            Task(id="T6", name="Copy Generation", depends_on=["T5"]),
        ]
