import time
from celery import Celery

app = Celery(
	'tasks', 
	backend='redis://localhost:6379/0', 
	broker='redis://localhost:6379/0')

@app.task(name='tasks.add')
def add(x, y):
	total = x + y
	print(f'{x} + {y} = {total}')
	time.sleep(10)
	return total


def backoff(attemps):
	"""
	1, 2, 4, 8, 16, 32
	"""
	return 2 ** attemps	


@app.task(bind=True, max_retries=4, soft_time_limit=5)
def data_extractor(self):
	try:
		for i in range(1, 11):
			print('Crawling HTML DOM!')
			if i == 5:
				raise ValueError('Crawling Index Error')
	except Exception as e:
		print(f'There was an exception <{e}> lets retry after 5 seconds')
		# raise self.retry(exc=e, countdown=5) 
		raise self.retry(exc=e, countdown=backoff(self.request.retries))	
