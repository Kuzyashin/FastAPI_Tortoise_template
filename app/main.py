from fastapi import FastAPI
from app.settings.config import settings


from app.core.init_app import init_app


app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.VERSION
)

init_app(app)
