from hello_world_for_django.celery import app


@app.task()
def run():
    print('hello')
