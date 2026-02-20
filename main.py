# =====================================================
# Jarvis Marketing Brain - Main Application
# =====================================================
import asyncio
from app.core.autonomy.goal_aging_engine import goal_aging_engine
from fastapi import FastAPI
import threading
from app.core.strategy.growth_scheduler import growth_scheduler
from app.core.strategy.allocation_scheduler import allocation_scheduler
from app.core.executive.policy_scheduler import policy_scheduler
from app.core.orchestrator.orchestrator_scheduler import orchestrator_scheduler
from app.core.reflection.reflection_scheduler import reflection_scheduler
from app.monitoring.production_routes import router as ops_router
from app.core.incidents.incident_scheduler import incident_scheduler

# -----------------------------------------------------
# CREATE FASTAPI APP FIRST (ALWAYS FIRST)
# -----------------------------------------------------
app = FastAPI(
    title="Jarvis Marketing Brain",
    version="0.1.0"
)

app = FastAPI(
    title="Jarvis Marketing Brain",
    version="0.1.0"
)

# Attach routes AFTER app creation
app.include_router(ops_router)

# ---- Core Systems ----
from app.core.learning_loop import ContinuousLearning
from app.observers.observer_runner import start_observers
from app.workflow.approval_routes import router as approval_router
from app.workflow.routes import router as workflow_router

# ---- OPTIONAL SYSTEMS (SAFE IMPORTS) ----
try:
    from app.monitoring.brain_routes import router as brain_router
    app.include_router(brain_router)
    print("✅ Brain Monitor Loaded")
except Exception as e:
    print("⚠️ Brain monitor disabled:", e)

# -----------------------------------------------------
# START BACKGROUND SYSTEMS
# -----------------------------------------------------
# -----------------------------------------------------
# START BACKGROUND SYSTEMS
# -----------------------------------------------------
@app.on_event("startup")
async def startup_systems():
   asyncio.create_task(incident_scheduler.run_loop())
   print("🛡 Incident Response System Started")

    asyncio.create_task(reflection_scheduler.run_loop())
    print("🪞 Self Reflection Engine Started")
    
    asyncio.create_task(orchestrator_scheduler.run_loop())
    print("🧠 Cognitive Orchestrator Started")

    asyncio.create_task(policy_scheduler.run_loop())
    print("🎯 Executive Decision Policy Started")

    asyncio.create_task(allocation_scheduler.run_loop())
    print("🧭 Strategic Resource Allocator Started")
    # ---------------------------------
    # Strategic Growth Scheduler
    # ---------------------------------
    asyncio.create_task(growth_scheduler.run_loop())
    print("📈 Growth Strategy Scheduler Started")

    # ---------------------------------
    # Observer Loop
    # ---------------------------------
    asyncio.create_task(start_observers())
    print("👁️ Observer system started")

    # ---------------------------------
    # Continuous Learning Thread
    # ---------------------------------
    def start_learning_loop():
        ContinuousLearning.run_loop()

    threading.Thread(
        target=start_learning_loop,
        daemon=True
    ).start()

    print("🚀 Background Learning Thread Started")

    # ---------------------------------
    # Goal Aging Background Loop
    # ---------------------------------
    async def aging_loop():
        while True:
            try:
                goal_aging_engine.run_cycle()
                print("[Aging] cycle executed")
            except Exception as e:
                print("[Aging ERROR]", e)

            await asyncio.sleep(300)  # every 5 minutes

    asyncio.create_task(aging_loop())
    print("🧠 Goal Aging System Started")
