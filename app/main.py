import logging

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.settings.config import settings


logging.config.fileConfig('app/settings/logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.VERSION
)

register_tortoise(
    app,
    db_url=settings.DB_URL,
    modules={"models": ["app.models.db.__init__"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
