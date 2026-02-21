from fastapi import FastAPI
import asyncio

from app.observer.observer_router import router as observer_router

app.include_router(observer_router)

# create app ONLY ONCE
app = FastAPI()

# import router AFTER app creation
from app.api.status import router as status_router

# register router
app.include_router(status_router)


# -------------------------
# ROOT ENDPOINT
# -------------------------
@app.get("/")
async def root():
    return {"message": "Jarvis Core Online"}


# -------------------------
# HEALTH CHECK
# -------------------------
@app.get("/health")
async def health():
    return {"status": "ok"}


# -------------------------
# HEARTBEAT LOOP
# -------------------------
async def heartbeat():
    while True:
        print("[HEARTBEAT] Core alive...")
        await asyncio.sleep(30)


# -------------------------
# STARTUP EVENT
# -------------------------
@app.on_event("startup")
async def start_heartbeat():
    asyncio.create_task(heartbeat())