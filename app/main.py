import os
import asyncio
import uvicorn
import logging
from fastapi import FastAPI
from typing import AsyncGenerator, Optional
from contextlib import asynccontextmanager
from dotenv import load_dotenv, find_dotenv
from fastapi import APIRouter

# services
from app.core.logging import setup_logging, logger
from app.services.monitoring.manager import MonitoringService

setup_logging()


# load environment variables
env_file = find_dotenv()
if env_file:
    load_dotenv(env_file)



@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Initialize
    try:
        monitoring_service = MonitoringService()
        monitoring_task = asyncio.create_task(monitoring_service.start_monitoring())        
        
        yield  
        
        logger.info("Shutting down monitoring task...")
        monitoring_task.cancel()
    except Exception as ex:
        logger.error(str(ex))

app = FastAPI(lifespan=lifespan)


main_router = APIRouter(prefix="/api/v1")

# main_router.include_router(avatars.router)    
# main_router.include_router(knowledge_base.router)
# main_router.include_router(rag.router)
# app.include_router(main_router)


