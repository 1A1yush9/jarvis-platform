# app/core/client_acquisition.py

from datetime import datetime
from typing import Dict, Any, List
import threading
import time
import random


class ClientAcquisitionEngine:
    """
    Stage 9.2 — Autonomous Client Acquisition Engine

    Generates structured client opportunities aligned
    with enterprise and revenue strategy direction.
    """

    def __init__(self, enterprise_controller=None, revenue_command=None):
        self.active = True
        self.enterprise_controller = enterprise_controller
        self.revenue_command = revenue_command

        self.state = {
            "mode": "scanning",
            "last_scan": None,
            "active_icp": "digital_business",
        }

        self.lead_queue: List[Dict[str, Any]] = []
        self.discovery_history: List[Dict[str, Any]] = []

        self.thread = threading.Thread(
            target=self._acquisition_loop,
            daemon=True
        )
        self.thread.start()

    # ---------------------------------------------------
    # MAIN LOOP
    # ---------------------------------------------------
    def _acquisition_loop(self):
        while self.active:
            try:
                lead = self._generate_opportunity()
                self.lead_queue.append(lead)
                self.discovery_history.append(lead)

                if len(self.discovery_history) > 150:
                    self.discovery_history.pop(0)

                self.state["last_scan"] = lead["timestamp"]

                print(f"[ClientAcquisition] Lead discovered → {lead['industry']}")

                time.sleep(40)  # Render-safe pacing

            except Exception as e:
                print(f"[ClientAcquisition ERROR] {e}")
                time.sleep(12)

    # ---------------------------------------------------
    # OPPORTUNITY GENERATION
    # ---------------------------------------------------
    def _generate_opportunity(self) -> Dict[str, Any]:

        enterprise_mode = "growth"
        if self.enterprise_controller:
            enterprise_mode = self.enterprise_controller.enterprise_state.get(
                "mode", "growth"
            )

        industries_growth = [
            "ecommerce",
            "education",
            "saas",
            "healthcare",
            "local_business_marketing"
        ]

        industries_defensive = [
            "existing_client_expansion",
            "retention_programs",
            "service_upsell"
        ]

        industry = random.choice(
            industries_growth if enterprise_mode != "defensive"
            else industries_defensive
        )

        lead = {
            "timestamp": datetime.utcnow().isoformat(),
            "industry": industry,
            "geo_target": random.choice(
                ["India", "UAE", "UK", "USA", "APAC"]
            ),
            "estimated_value": random.randint(1500, 12000),
            "confidence_score": random.randint(65, 96),
            "source": "Client Acquisition Engine"
        }

        return lead

    # ---------------------------------------------------
    # PUBLIC STATUS
    # ---------------------------------------------------
    def get_status(self) -> Dict[str, Any]:
        return {
            "acquisition_active": self.active,
            "state": self.state,
            "lead_queue_size": len(self.lead_queue),
            "history_size": len(self.discovery_history)
        }

    def shutdown(self):
        self.active = False