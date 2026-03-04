from typing import Dict


class InfluenceRebalanceModel:
    """
    Determines governance influence adjustments.
    """

    def rebalance(self, signals: Dict, fault_domain_status: Dict) -> Dict:

        isolated_nodes = fault_domain_status.get("isolated_nodes", [])

        action = "NO_ACTION"

        if signals["stabilization_required"]:

            if isolated_nodes:
                action = "REDUCE_INFLUENCE_OF_ISOLATED_NODES"
            else:
                action = "TEMPORARY_CONSENSUS_TIGHTENING"

        return {
            "recommended_action": action,
            "isolated_nodes": isolated_nodes
        }