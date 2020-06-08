import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.settings.config import settings
from app.settings.log import DEFAULT_LOGGING


def configure_logging(log_settings: dict = None):
    log_settings = log_settings or DEFAULT_LOGGING
    logging.config.dictConfig(log_settings)


def init_middlewares(app: FastAPI):
    logging.config.dictConfig(DEFAULT_LOGGING)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
    )


def register_db(app: FastAPI, db_url: str = None):
    db_url = db_url or settings.DB_URL

    register_tortoise(
        app,
        db_url=db_url,
        modules={"models": ["app.models.db.__init__"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
