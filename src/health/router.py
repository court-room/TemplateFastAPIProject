from fastapi import APIRouter

from src.health.schema import Healthcheck

router = APIRouter()


@router.get("/health")
async def healthcheck() -> Healthcheck:
    return Healthcheck(status="OK", checks=[])
