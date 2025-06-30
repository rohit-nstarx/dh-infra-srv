from fastapi import APIRouter
from app.core.logging import logger
from app.core.shared import ServiceStatusStore

services_router = APIRouter(tags=["Services"])

@services_router.get("/status")
async def service_status():
    return await ServiceStatusStore.get_all_statuses()

