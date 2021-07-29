import threading 
from random import randint
from time import sleep
from queue import Queue


NUMBER_ITEMS_TO_PUT_OR_GET_TOGETHER: int = 2

queue_resource = Queue()

condition = threading.Condition()

def is_queue_size_greather_than_amount(amount: int = NUMBER_ITEMS_TO_PUT_OR_GET_TOGETHER):

	return len(queue_resource.queue) >= amount

def producer(n_items: int = NUMBER_ITEMS_TO_PUT_OR_GET_TOGETHER) -> None:	

	for _ in range(2):

		sleep(1)

		condition.acquire()

		for i in range(n_items):

			sleep(1)

			resource: str = f'resource_{randint(0, 100)}'

			queue_resource.put(resource)

			print(f'producer {threading.current_thread().name} -> {resource} produced')

		condition.notify_all()

		# condition.notify(n=NUMBER_ITEMS_TO_PUT_OR_GET_TOGETHER) # works the same

		condition.release()


def consumer(n_items: int = NUMBER_ITEMS_TO_PUT_OR_GET_TOGETHER) -> None:
	"""n_items: number fo items to consume together"""

	condition.acquire()

	print(f'consumer {threading.current_thread().name} -> waiting resource')	

	condition.wait_for(predicate=is_queue_size_greather_than_amount)

	consumed_resources: list = [queue_resource.get(), queue_resource.get()]

	print(f'consumer {threading.current_thread().name} -> {consumed_resources} consumed')

	condition.release()


thread_producer = threading.Thread(name='thread_producer', target=producer)

thread_consumer_1 = threading.Thread(name='thread_consumer_1', target=consumer)

thread_consumer_2 = threading.Thread(name='thread_consumer_2', target=consumer)

thread_consumer_1.start()

thread_consumer_2.start()

thread_producer.start()
