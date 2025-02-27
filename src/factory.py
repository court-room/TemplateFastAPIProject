from fastapi import FastAPI

from src.health.router import router as health_router


def app_factory() -> FastAPI:
    app = FastAPI()

    app.include_router(health_router, tags=["health"])

    return app
