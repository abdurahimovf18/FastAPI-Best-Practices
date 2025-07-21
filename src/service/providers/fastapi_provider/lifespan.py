import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initsalizing FastAPI application")
    logger.info(f"FastAPI application: {app}")
    
    yield

    logger.info("Closing FastAPI application")