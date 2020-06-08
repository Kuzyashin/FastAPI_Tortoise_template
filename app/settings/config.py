import os


class Settings:
    VERSION = '0.1.0'
    APP_TITLE = 'Template Application'
    APP_DESCRIPTION = 'TG - @AKuzyashin\nhttps://github.com/Kuzyashin'
    DB_URL = 'sqlite://./test.db'
    DEBUG = False
    RABBIT_LOGIN = 'guest'
    RABBIT_PASSWORD = ''
    RABBIT_HOST = 'localhost'

    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))
    LOGS_ROOT = os.path.join(BASE_DIR, "app/logs")


settings = Settings()
