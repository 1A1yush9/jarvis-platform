from fastapi import FastAPI
import asyncio

app = FastAPI()


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