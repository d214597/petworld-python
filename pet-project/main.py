import logging
from contextlib import asynccontextmanager
from core.models import db_helper
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from api import router as api_router
from logging_config import configure_logging
from utils.timing import log_requests, measure_time

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    logger.info("LOGGING CONFIGURED!")
    yield
    await db_helper.dispose()

main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

main_app.include_router(api_router)


main_app.middleware("http")(log_requests)


@main_app.get("/example")
@measure_time
async def example_endpoint():
    return {"message": "This is an example"}
