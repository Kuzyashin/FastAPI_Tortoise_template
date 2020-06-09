# Базовый шаблон FastAPI
## Включает в себя
### - FastAPI
### - TortoiseORM
### - User model + JWT auth
### - Registration + password reset emails
### - Logging to files

# Установка
### Скопировать template.config.py -> config.py и заполнить
### Прописать все app в config.applications (django style) поиск моделей будет происходить по пути app.applications.APP_NAME.models
### Сгенерировать SECRET_KEY ( можно командой `openssl rand -hex 32`)
