# !/usr/bin/python3
import time

from celery import Celery, shared_task, Task
from celery.exceptions import SoftTimeLimitExceeded
from celery.schedules import crontab

app = Celery('tasks',
             broker='redis://localhost:6379',
             backend='redis://localhost:6379',
             # include=['other_tasks'],
             )

# app.conf.update({'worker_max_tasks_per_child': 1})
#
# @app.on_after_configure.connect
# # @app.on_after_finalize.connect()
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, hello.s(), name='add every 10')
#
#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, hello.s(), expires=10)
#
#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1),
#         hello.s(),
#     )

#
# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'tasks.hello',
#         'schedule': 10.0,
#     },
# }
# app.conf.timezone = 'UTC'

# app.conf.task_routes = {'tasks.*': {'queue': 'feeds'}}

# app.conf.task_routes = {'tasks.long_task': {'queue': 'slows'},
#                         'tasks.short_task': {'queue': 'feeds'}}


@app.task()
def hello():
    print('hello')


@shared_task()
def hello_share():
    print('hello share')


class TaskBase(Task):
    def __init__(self):
        self.a = self.load_model()

    def on_success(self, retval, task_id, args, kwargs):
        print('task success')

    def load_model(self):
        # time.sleep(5)
        return 'a word'


@app.task(base=TaskBase)
def try_load_base():
    print('do something')
    print('a is %s' % try_load_base.a)


@app.task(soft_time_limit=1)
def soft_time_limit_task():
    try:
        time.sleep(5)
    except SoftTimeLimitExceeded:
        print('do something')


@app.task(time_limit=1)
def time_limit_task():
    time.sleep(5)


@app.task(autoretry_for=(ZeroDivisionError,))
def task_auto_retry():
    print(1/0)


@app.task(acks_late=True)
def task_auto_ack_late():
    print(1111111)
    print(1/0)


@app.task(bind=True)
def task_update_stats(self):
    for i in range(10):
        self.update_state(state='PROGRESS',
                          meta={'current': i*10, 'total': 100})
        time.sleep(1)


@app.task()
def task_eta():
    print('task start')


@app.task()
def add(a, b):
    return a + b


@app.task()
def sub(a, b):
    return a - b


@app.task()
def div(x, y):
    return x % y


@app.task()
def find_zero(num_list, i):
    if 0 in num_list:
        return None
    else:
        return i


@app.task()
def long_task():
    print('long task start')
    time.sleep(60)
    print('long task done')


@app.task()
def short_task():
    print('short task start')
    print('short task done')
