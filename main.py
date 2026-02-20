# =====================================================
# Jarvis Marketing Brain - SAFE CORE BOOT
# =====================================================

import asyncio
from fastapi import FastAPI

# -----------------------------------------------------
# CREATE FASTAPI APP
# -----------------------------------------------------
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
            print("❤️ Jarvis alive")
            await asyncio.sleep(20)

    asyncio.create_task(heartbeat())

    print("✅ SAFE CORE READY")


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