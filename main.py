# =====================================================
# Jarvis Marketing Brain - Main Application
# =====================================================
import asyncio
import threading
from fastapi import FastAPI

# ---- Core Engines ----
from app.core.autonomy.goal_aging_engine import goal_aging_engine
from app.core.strategy.growth_scheduler import growth_scheduler
from app.core.strategy.allocation_scheduler import allocation_scheduler
from app.core.executive.policy_scheduler import policy_scheduler
from app.core.orchestrator.orchestrator_scheduler import orchestrator_scheduler
from app.core.reflection.reflection_scheduler import reflection_scheduler
from app.core.incidents.incident_scheduler import incident_scheduler

# ---- Routes ----
from app.monitoring.production_routes import router as ops_router
from app.workflow.approval_routes import router as approval_router
from app.workflow.routes import router as workflow_router

# ---- Learning + Observers ----
from app.core.learning_loop import ContinuousLearning
from app.observers.observer_runner import start_observers


# =====================================================
# CREATE FASTAPI APP (ONLY ONCE)
# =====================================================
app = FastAPI(
    title="Jarvis Marketing Brain",
    version="0.1.0"
)

# Attach routers
app.include_router(ops_router)
app.include_router(approval_router)
app.include_router(workflow_router)

# Optional monitoring routes
try:
    from app.monitoring.brain_routes import router as brain_router
    app.include_router(brain_router)
    print("✅ Brain Monitor Loaded")
except Exception as e:
    print("⚠️ Brain monitor disabled:", e)


# =====================================================
# SAFE TASK STARTER (prevents Render crashes)
# =====================================================
def safe_task(coro, name: str):
    async def runner():
        while True:
            try:
                await coro()
            except Exception as e:
                print(f"[ERROR] {name} crashed:", e)
                await asyncio.sleep(10)

    asyncio.create_task(runner())


# =====================================================
# STARTUP SYSTEMS (Render Safe)
# =====================================================
@app.on_event("startup")
async def startup_systems():

    print("🚀 Jarvis Startup Initiated")

    # ---- Schedulers ----
    safe_task(incident_scheduler.run_loop, "Incident Scheduler")
    safe_task(reflection_scheduler.run_loop, "Reflection Engine")
    safe_task(orchestrator_scheduler.run_loop, "Orchestrator")
    safe_task(policy_scheduler.run_loop, "Policy Engine")
    safe_task(allocation_scheduler.run_loop, "Allocation Engine")
    safe_task(growth_scheduler.run_loop, "Growth Scheduler")

    # ---- Observers ----
    asyncio.create_task(start_observers())
    print("👁️ Observer system started")

    # ---- Continuous Learning (Thread) ----
    def start_learning_loop():
        try:
            ContinuousLearning.run_loop()
        except Exception as e:
            print("[Learning ERROR]", e)

    threading.Thread(
        target=start_learning_loop,
        daemon=True
    ).start()

    print("🧠 Learning Thread Started")

    # ---- Goal Aging Loop ----
    async def aging_loop():
        while True:
            try:
                goal_aging_engine.run_cycle()
                print("[Aging] cycle executed")
            except Exception as e:
                print("[Aging ERROR]", e)

            await asyncio.sleep(300)

    asyncio.create_task(aging_loop())
    print("🧬 Goal Aging System Started")


# =====================================================
# BASIC HEALTH ROUTES (VERY IMPORTANT)
# =====================================================
@app.get("/")
async def root():
    return {"status": "Jarvis running"}


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "jarvis-platform"
    }