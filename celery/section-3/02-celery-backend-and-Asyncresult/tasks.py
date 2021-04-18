import time
from celery import Celery


app = Celery('tasks', backend=None, broker='redis://localhost:6379/0')
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'

@app.task(name='tasks.add')
def add(x, y):
	total = x + y
	print(f'{x} + {y} = {total}')
	time.sleep(10)
	return total
