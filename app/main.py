from fastapi import FastAPI
from app.settings.config import settings


from app.core.init_app import configure_logging, init_middlewares, register_db

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.VERSION
)


configure_logging()
init_middlewares(app)
register_db(app)
