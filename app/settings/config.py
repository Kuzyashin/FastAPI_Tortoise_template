import os


class Settings:
    VERSION = '0.1.0'
    APP_TITLE = 'Template Application'
    APP_DESCRIPTION = 'TG - @AKuzyashin\nhttps://github.com/Kuzyashin'

    DB_URL = 'sqlite://./test.db'

    DEBUG = True

    RABBIT_LOGIN = 'guest'
    RABBIT_PASSWORD = ''
    RABBIT_HOST = 'localhost'

    REDIS_URL = ''

    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))
    LOGS_ROOT = os.path.join(BASE_DIR, "app/logs")

    CORS_ORIGINS = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:5000",
        "http://localhost:3000",
    ]
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_METHODS = ["*"]
    CORS_ALLOW_HEADERS = ["*"]


settings = Settings()
