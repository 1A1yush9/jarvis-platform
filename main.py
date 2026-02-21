# main.py  (ROOT ENTRY FILE FOR RENDER)

"""
Jarvis Render Entry Point
DO NOT place logic here.

This file only exposes the FastAPI app
from app.main so Render can start safely.
"""

from app.main import app

# Optional local run support
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=10000,
        reload=False
    )