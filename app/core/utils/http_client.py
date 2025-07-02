import httpx
import os
import logging
from typing import Any, Dict, Optional
from app.core.logging import logger
from app.config import env_var


class AsyncHttpClient:
    def __init__(self, timeout: Optional[float] = env_var.HTTP_REQUEST_TIMEOUT):
        self.timeout = timeout

    async def __aenter__(self):
        self.client = httpx.AsyncClient(timeout=self.timeout)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()

    async def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Optional[httpx.Response]:
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, params=params, headers=headers)
                logger.debug("url: %s -  status code: %s", url, response.status_code)
                # logger.debug("response text: %s", response.text)
                response.raise_for_status()
                return response
        except Exception as ex:
            raise ex

    async def post(
        self,
        url: str,
        data: Optional[Any] = None,
        json: Optional[Any] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Optional[httpx.Response]:
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(url, data=data, json=json, headers=headers)
                logger.debug("url %s - status code: %s", url, response.status_code)
                logger.debug("response text: %s", response.text)
                response.raise_for_status()
                return response
        except Exception as ex:
            raise ex
