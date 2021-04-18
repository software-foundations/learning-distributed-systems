import time
from tasks import add
from celery.result import AsyncResult


result = add.delay(1, 2)

while True:
	_result2 = AsyncResult(result.task_id)
	status = _result2.status
	print(status)
	if 'SUCCESS' in status:
		print(f'result after 5 sec wait {_result2.get()}')
		break
	time.sleep(5)