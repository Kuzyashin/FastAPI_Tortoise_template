# Базовый шаблон FastAPI
### Включает в себя
#### - FastAPI
#### - TortoiseORM
#### - Aerich
#### - User model + JWT auth
#### - Registration + password reset emails
#### - Logging to files
#### - Celery
#### - Alpine Dockerfile
#### - Docker-compose files
#### - NGINX + certbot

# Установка
#### Скопировать template.config.py -> config.py и заполнить
#### Прописать все app в config.applications (django style). Поиск моделей будет происходить по пути app.applications.APP_NAME.models
#### Сгенерировать SECRET_KEY ( можно командой `openssl rand -hex 32`)
#### Так-же можно сгенерить сертификаты скриптом из репы ( #TODO гайд )
