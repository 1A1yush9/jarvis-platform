# =====================================================
# Jarvis Marketing Brain - SAFE CORE BOOT
# =====================================================

import asyncio
from fastapi import FastAPI

# -----------------------------------------------------
# CREATE FASTAPI APP
# -----------------------------------------------------
from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Jarvis Core Online"}


@app.get("/health")
async def health():
    return {"status": "ok"}

    app = FastAPI(
    title="Jarvis Marketing Brain",
    version="0.1.0"
)

# -----------------------------------------------------
# STARTUP (SAFE MODE ONLY)
# -----------------------------------------------------
@app.on_event("startup")
async def startup():

    print("🚀 SAFE CORE BOOT STARTED")

    async def heartbeat():
    while True:
        print("[HEARTBEAT] Core alive...")
        await asyncio.sleep(30)


@app.on_event("startup")
async def start_heartbeat():
    asyncio.create_task(heartbeat())


# -----------------------------------------------------
# BASIC ROUTES
# -----------------------------------------------------
@app.get("/")
async def root():
    return {"status": "Jarvis running"}


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "jarvis-platform"
    }