from fastapi import FastAPI
from app.routers import health

def create_app() -> FastAPI:
    app = FastAPI(title="New One.UF", version="0.1.0")
    app.include_router(health.router, prefix="/v1")
    return app

app = create_app()