from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health
from app.config.settings import settings

def create_app() -> FastAPI:
    api = FastAPI(title="New One.UF", version="0.1.0")
    
    api.add_middleware(
        CORSMiddleware,
        allow_origins=settings.FRONTEND_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    api.include_router(health.router, prefix="/v1")
    return api

app = create_app()