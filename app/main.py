import os
import asyncio
import uvicorn
import logging
from fastapi import FastAPI
from typing import AsyncGenerator, Optional
from contextlib import asynccontextmanager
from fastapi import APIRouter
from app.routes.base import router
from app.routes.services_router import services_router
from app.routes.avatar_router import avatar_router
from app.routes.knowledge_base_router import knowlege_router
from app.routes.conversation_router import conversation_router

# database
from app.core.db.connections.postgres import engine, Base

# services
from app.core.logging import setup_logging, logger
from app.services.monitoring.monitor import MonitoringService
from app.services.startup_checker import initialization_check



setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Initialize
    try:
        # wait for initialization to complete
        await initialization_check()

        # create required tables
        Base.metadata.create_all(engine)

        monitoring_service = MonitoringService()
        monitoring_task = asyncio.create_task(monitoring_service.start_monitoring())

        yield

        logger.info("Shutting down monitoring task...")
        monitoring_task.cancel()
    except Exception as ex:
        logger.error(str(ex))
        raise ex


app = FastAPI(lifespan=lifespan, title="DH Infra Service")


main_router = APIRouter(prefix="/api/v1")
main_router.include_router(router)

data_router = APIRouter(prefix="/data", tags=["Data Store"])
data_router.include_router(avatar_router)
data_router.include_router(knowlege_router)
data_router.include_router(conversation_router)


main_router.include_router(data_router)
main_router.include_router(services_router, prefix="/services")
app.include_router(main_router)


