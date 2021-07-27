import time
from celery import Celery
import redis


# DEPRECATED
# https://stackoverflow.com/questions/64483648/django-and-celery-modulenotfounderror-no-module-named-celery-task
# from celery.decorators import periodic_task

# TRYING TO SOLVE
from celery.schedules import crontab
from datetime import timedelta


app = Celery(
	'tasks', 
	backend='redis://localhost:6379/0', 
	broker='redis://localhost:6379/0')

# TRYING TO SOLVE
app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'tasks.add',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
}

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


# @periodic_task(run_every=timedelta(seconds=3), name='tasks.send_mail_from_queue')
@periodic_task(run_every=timedelta(seconds=3), name='tasks.send_mail_from_queue')
def send_mail_from_queue():
	try:
		messages_sent = "example.email"
		print(f"email message sucessfully sent, [{messages_sent}]")
	finally:
		print("release resources")