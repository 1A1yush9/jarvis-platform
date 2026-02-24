# =====================================================
# Jarvis Core Orchestrator
# Central Autonomous Marketing Brain
# =====================================================

from app.core.audience_brain import AudienceBrain
from app.core.messaging_brain import MessagingBrain
from app.core.market_brain import MarketBrain
from app.core.creative_brain import CreativeBrain
from app.core.optimizer_brain import OptimizerBrain
from app.core.budget_brain import BudgetBrain
from app.core.predictive_brain import PredictiveBrain
from app.core.strategy_brain import StrategyBrain
from app.core.memory import MemoryBrain, MemoryStore
from app.core.database import SessionLocal
from app.core.intent_parser import IntentParser
from app.core.objective import ObjectiveBuilder
from app.core.task_graph import TaskGraphBuilder
from app.core.dispatcher import Dispatcher


class JarvisCore:

    def __init__(self):
        self.intent_parser = IntentParser()
        self.objective_builder = ObjectiveBuilder()
        self.task_graph_builder = TaskGraphBuilder()
        self.dispatcher = Dispatcher()
        self.memory = MemoryStore()

    # =================================================
    # MAIN EXECUTION
    # =================================================
    def run(self, user_input: str):

        db = SessionLocal()

        # -----------------------------
        # INTENT + OBJECTIVE
        # -----------------------------
        intent = self.intent_parser.parse(user_input)
        objective = self.objective_builder.build(intent)

        # -----------------------------
        # STRATEGY + PREDICTION
        # -----------------------------
        strategy_plan = StrategyBrain.get_best_strategy(
            db, intent.industry
        )

        prediction = PredictiveBrain.predict_campaign(
            db, intent.industry
        )

        # -----------------------------
        # MARKET AWARENESS
        # -----------------------------
        market_context = MarketBrain.get_market_context()

        # -----------------------------
        # BUDGET DECISION
        # -----------------------------
        budget_plan = BudgetBrain.optimize_budget(
            strategy_plan,
            prediction
        )

        # -----------------------------
        # ADAPTIVE MESSAGING (STEP 4.37)
        # -----------------------------
        messaging_style = MessagingBrain.decide_tone(
            prediction,
            budget_plan,
            market_context
        )

        # -----------------------------
        # AUDIENCE INTELLIGENCE (STEP 4.38)
        # -----------------------------
        audience_profile = AudienceBrain.detect_audience(
            intent,
            budget_plan,
            strategy_plan
        )

        # -----------------------------
        # CREATIVE INTELLIGENCE
        # -----------------------------
        best_creatives = CreativeBrain.get_best_creatives(
            db,
            intent.industry
        )

        # -----------------------------
        # MEMORY LEARNING
        # -----------------------------
        similar_campaigns = MemoryBrain.find_similar(
            db,
            intent.industry
        )

        learning_context = ""

        if similar_campaigns:
            learning_context += "\nPast successful strategies:\n"
            for s in similar_campaigns:
                learning_context += f"- {s.generated_strategy}\n"

        tasks = self.task_graph_builder.build()
        results = []

        # =================================================
        # EXECUTION LOOP
        # =================================================
        for task in tasks:

            context = {
                "industry": intent.industry,
                "location": intent.location,
                "learning_context": learning_context,
                "strategy_plan": strategy_plan,
                "prediction": prediction,
                "budget_plan": budget_plan,
                "market_context": market_context,
                "messaging_style": messaging_style,
                "audience_profile": audience_profile,
                "best_creatives": best_creatives
            }

            # carry leads forward
            for r in results:
                if "leads" in r.get("output", {}):
                    context["leads"] = r["output"]["leads"]

            jarvis_unit = self.dispatcher.assign(task)
            output = jarvis_unit.execute(task, context=context)

            task.status = "completed"

            results.append({
                "task_id": task.id,
                "task_name": task.name,
                "jarvis": jarvis_unit.name,
                "output": output
            })

        # =================================================
        # ROI + OPTIMIZER
        # =================================================
        simulated_roi = prediction["predicted_roi"]

        optimizer_decision = OptimizerBrain.evaluate_campaign(
            prediction,
            simulated_roi
        )

        adjusted_budget = int(
            budget_plan["total_budget"]
            * optimizer_decision["budget_multiplier"]
        )

        budget_plan["adjusted_budget"] = adjusted_budget
        budget_plan["optimizer_action"] = optimizer_decision["action"]
        budget_plan["optimizer_reason"] = optimizer_decision["reason"]

        # =================================================
        # SAVE LEARNING
        # =================================================
        MemoryBrain.store_campaign(
            db,
            {
                "business_type": intent.industry,
                "niche": intent.industry,
                "client_name": "unknown",
                "location": intent.location,
                "campaign_input": user_input,
                "generated_strategy": str(results),
                "channels_used": "Auto",
                "estimated_budget": adjusted_budget,
                "performance_score": simulated_roi
            }
        )

        # Creative learning
        CreativeBrain.learn_from_campaign(
            db,
            intent.industry,
            str(results)
        )

        CreativeBrain.update_creative_performance(
            db,
            intent.industry,
            simulated_roi
        )

        # Short-term memory snapshot
        self.memory.save({
            "industry": intent.industry,
            "location": intent.location,
            "objective": objective["primary_objective"],
            "tasks_completed": [r["task_name"] for r in results]
        })

        db.close()

        # =================================================
        # RESPONSE
        # =================================================
        return {
            "intent": intent.dict(),
            "objective": objective,
            "prediction": prediction,
            "market_context": market_context,
            "messaging_style": messaging_style,
            "audience_profile": audience_profile,
            "budget_plan": budget_plan,
            "optimizer_decision": optimizer_decision,
            "execution_results": results,
            "memory_snapshot": self.memory.all()
        }
