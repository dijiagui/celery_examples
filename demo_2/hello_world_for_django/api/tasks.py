from hello_world_for_django.celery import app
from celery.utils.log import get_task_logger

log = get_task_logger(__name__)


@app.task()
def run():
    log.info('hello')
