from tasks import app


@app.task()
def other_hello():
    print('hello from other task')