from fastapi import FastAPI
from app.core.exceptions import SettingNotFound
from app.core.init_app import configure_logging, init_middlewares, register_db, register_exceptions, register_routers

try:
    from app.settings.config import settings
except ImportError:
    raise SettingNotFound('Can not import settings. Create settings file from template.config.py')


app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.VERSION
)

configure_logging()
init_middlewares(app)
register_db(app)
register_exceptions(app)
register_routers(app)
