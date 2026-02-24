# =====================================================
# Jarvis Continuous Learning Loop
# =====================================================

import time
from app.core.database import SessionLocal
from app.core.memory_models import CampaignMemory


class ContinuousLearning:
    """
    Background intelligence evolution system.
    Rebalances strategy performance automatically.
    """

    @staticmethod
    def rebalance_performance(db):
        records = db.query(CampaignMemory).all()

        if not records:
            return

        # ---- calculate global average ----
        avg_score = sum(r.performance_score for r in records) / len(records)

        for r in records:

            # reward strong strategies
            if r.performance_score > avg_score:
                r.performance_score *= 1.05

            # decay weak strategies slowly
            else:
                r.performance_score *= 0.97

        db.commit()

    @staticmethod
    def run_loop(interval_seconds=300):
        """
        Infinite background learning cycle.
        Default: every 5 minutes (development safe)
        """

        print("🧠 Continuous Learning Loop Started")

        while True:
            db = SessionLocal()

            try:
                ContinuousLearning.rebalance_performance(db)
                print("✅ Jarvis learning cycle completed")

            except Exception as e:
                # prevents thread death
                print("❌ Learning loop error:", e)

            finally:
                db.close()

            time.sleep(interval_seconds)
