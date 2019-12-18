from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.signals import setup_logging


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'hello_world_for_django.settings')

app = Celery('hello_world_for_django', broker='redis://localhost:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')


@setup_logging.connect
def config_loggers(*args, **kwags):
    from logging.config import dictConfig
    from hello_world_for_django import settings
    dictConfig(settings.LOGGING)


# 自动加载django app中的任务，省略了写include
app.autodiscover_tasks()
