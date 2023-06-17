from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from .routes import router
from ..config import Config


logger = logging.getLogger(__name__)


def get_lifespan(_config: Config):
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        global logger
        logger = logging.getLogger(__name__)
        logger.info("Starting up")
        yield
        logger.info("Shutting down")

    return lifespan


def create_app(_config: Config):
    app = FastAPI(lifespan=get_lifespan(_config))
    app.state.config = _config
    app.include_router(router)
    return app
