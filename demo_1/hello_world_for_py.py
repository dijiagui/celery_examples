# !/usr/bin/python3

from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379')


@app.task(countdown=1)
def run():
    print('hello')