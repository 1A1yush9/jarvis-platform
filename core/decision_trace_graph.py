"""
Stage-41.0 — Executive Accountability & Decision Trace Graph

Creates traceable lineage for advisory intelligence.
Maintains explainability without enabling execution authority.
"""

from datetime import datetime
from typing import Dict, Any, List, Optional
import uuid


class DecisionNode:
    """
    Represents a single advisory reasoning event.
    """

    def __init__(
        self,
        title: str,
        payload: Dict[str, Any],
        confidence: float,
        parent_id: Optional[str] = None,
    ):
        self.id = str(uuid.uuid4())
        self.title = title
        self.payload = payload
        self.confidence = confidence
        self.parent_id = parent_id
        self.timestamp = datetime.utcnow().isoformat()
        self.oversight_id = None
        self.constitutional_status = None


class DecisionTraceGraph:
    """
    Maintains directed lineage of strategic reasoning.
    """

    def __init__(self):
        self.nodes: Dict[str, DecisionNode] = {}

    # ---------------------------------------------------------
    # Create Decision Node
    # ---------------------------------------------------------

    def create_node(
        self,
        title: str,
        payload: Dict[str, Any],
        confidence: float,
        parent_id: Optional[str] = None,
    ) -> Dict[str, Any]:

        node = DecisionNode(title, payload, confidence, parent_id)
        self.nodes[node.id] = node

        return {
            "decision_id": node.id,
            "timestamp": node.timestamp,
            "status": "RECORDED",
        }

    # ---------------------------------------------------------
    # Attach Oversight Reference
    # ---------------------------------------------------------

    def attach_oversight(
        self,
        decision_id: str,
        oversight_id: str,
    ):
        if decision_id in self.nodes:
            self.nodes[decision_id].oversight_id = oversight_id

    # ---------------------------------------------------------
    # Attach Constitutional Result
    # ---------------------------------------------------------

    def attach_constitutional_status(
        self,
        decision_id: str,
        status: str,
    ):
        if decision_id in self.nodes:
            self.nodes[decision_id].constitutional_status = status

    # ---------------------------------------------------------
    # Trace Lineage
    # ---------------------------------------------------------

    def get_trace(self, decision_id: str) -> List[Dict[str, Any]]:
        trace = []
        current = self.nodes.get(decision_id)

        while current:
            trace.append({
                "decision_id": current.id,
                "title": current.title,
                "confidence": current.confidence,
                "timestamp": current.timestamp,
                "oversight_id": current.oversight_id,
                "constitutional_status": current.constitutional_status,
            })
            current = self.nodes.get(current.parent_id)

        return list(reversed(trace))


# Singleton instance
decision_trace_graph = DecisionTraceGraph()