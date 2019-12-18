from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'hello_world_for_django.settings')

app = Celery('hello_world_for_django', broker='redis://localhost:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动加载django app中的任务，省略了写include
app.autodiscover_tasks()
