from __future__ import absolute_import, unicode_literals
from app.settings.config import settings

broker_url = 'amqp://{}:{}@{}:5672'.format(settings.RABBIT_LOGIN, settings.RABBIT_PASSWORD, settings.RABBIT_HOST)
accept_content = ['json']
enable_utc = False
task_serializer = 'json'
result_backend = 'redis://localhost'
timezone = 'UTC'
task_track_started = True
worker_hijack_root_logger = False
worker_redirect_stdouts_level = 'ERROR'
result_expires = 60 * 60 * 24
