from fastapi import FastAPI

from app.settings.config import settings
from app.applications.users import routes
from app.core.auth.routers.login import router as login_router
from app.applications.users.routes import router as users_router

from app.core.init_app import configure_logging, init_middlewares, register_db

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.VERSION
)


configure_logging()
init_middlewares(app)
register_db(app)

app.include_router(login_router, prefix='/api/auth/login')
app.include_router(users_router, prefix='/api/auth/users')
