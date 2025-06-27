import asyncio
from app.core.factory.embeddings_mapping import get_active_embedding
from app.core.factory.llm_mappings import get_active_llm
from app.core.factory.vector_strore_mappings import get_active_vector_store

from app.core.logging import logger
from app.config import env_var
from app.core.shared import ServiceStatusStore


services = [get_active_llm(), get_active_embedding(), get_active_vector_store()]


async def initialization_check():
    WAIT_FOR = 5

    logger.info("Active LLM: %s", env_var.ACTIVE_LLM)
    logger.info("Active Embeddings: %s", env_var.ACTIVE_EMBEDDING)
    logger.info("Active Vector Store: %s", env_var.ACTIVE_VECTOR_STORE)

    for i in range(1, 10):
        logger.info(f"Attempt {i}/9")
        tasks = [service.is_ready() for service in services]
        results = await asyncio.gather(*tasks)
        for service, result in zip(services, results):
            logger.info(f"{service.__class__.__name__}: {result}")
            await ServiceStatusStore.set_status(
                service_name=service.__class__.__name__, status=result
            )

        if all(results):
            logger.info("All services are ready.")
            return

        logger.info(f"retrying after {i * WAIT_FOR} seconds...")
        await asyncio.sleep(i * WAIT_FOR)

    raise RuntimeError(f"Startup failed. Unhealthy services")
