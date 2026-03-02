"""
Stage-48.0 — Strategic Awareness Graph

Creates relationship mapping across advisory intelligence
components (memory, decisions, forecasts, consensus, intent).

Advisory metadata only. No execution authority.
"""

from datetime import datetime
from typing import Dict, Any, List
import uuid


class AwarenessNode:
    def __init__(self, node_type: str, reference_id: str, metadata: Dict[str, Any]):
        self.id = str(uuid.uuid4())
        self.node_type = node_type
        self.reference_id = reference_id
        self.metadata = metadata
        self.created_at = datetime.utcnow().isoformat()


class AwarenessEdge:
    def __init__(self, source: str, target: str, relation: str):
        self.id = str(uuid.uuid4())
        self.source = source
        self.target = target
        self.relation = relation
        self.created_at = datetime.utcnow().isoformat()


class StrategicAwarenessGraph:

    def __init__(self):
        self.nodes: Dict[str, AwarenessNode] = {}
        self.edges: List[AwarenessEdge] = []

    # ---------------------------------------------------------
    # Create Node
    # ---------------------------------------------------------

    def create_node(
        self,
        node_type: str,
        reference_id: str,
        metadata: Dict[str, Any],
    ) -> Dict[str, Any]:

        node = AwarenessNode(node_type, reference_id, metadata)
        self.nodes[node.id] = node

        return {
            "node_id": node.id,
            "status": "NODE_CREATED",
        }

    # ---------------------------------------------------------
    # Link Nodes
    # ---------------------------------------------------------

    def link_nodes(
        self,
        source_node_id: str,
        target_node_id: str,
        relation: str,
    ) -> Dict[str, Any]:

        if source_node_id not in self.nodes or target_node_id not in self.nodes:
            return {"error": "Node not found"}

        edge = AwarenessEdge(source_node_id, target_node_id, relation)
        self.edges.append(edge)

        return {
            "edge_id": edge.id,
            "status": "LINK_CREATED",
        }

    # ---------------------------------------------------------
    # Retrieve Graph Snapshot
    # ---------------------------------------------------------

    def snapshot(self):

        return {
            "nodes": [
                {
                    "node_id": n.id,
                    "type": n.node_type,
                    "reference_id": n.reference_id,
                    "metadata": n.metadata,
                }
                for n in self.nodes.values()
            ],
            "edges": [
                {
                    "edge_id": e.id,
                    "source": e.source,
                    "target": e.target,
                    "relation": e.relation,
                }
                for e in self.edges
            ],
            "total_nodes": len(self.nodes),
            "total_edges": len(self.edges),
        }


# Singleton instance
strategic_awareness_graph = StrategicAwarenessGraph()