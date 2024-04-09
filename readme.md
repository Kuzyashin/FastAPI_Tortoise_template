# Basic FastAPI Template
### Includes
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

# Installation
#### Copy template.config.py -> config.py and fill in
#### Specify all apps in config.applications (django style). Model searching will be performed in the path app.applications.APP_NAME.models
#### Generate SECRET_KEY (can be done with the command `openssl rand -hex 32`)
#### Certificates can also be generated with a script from the repo ( #TODO guide )