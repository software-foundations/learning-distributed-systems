from celery import Celery


app = Celery('tasks', backend=None, broker='redis://localhost:6379/0')


@app.task(name='tasks.add')
def add(x, y):
	print(f'{x} + {y} = {x + y}')