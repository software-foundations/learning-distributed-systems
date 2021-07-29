import threading 
from random import randint
from time import sleep
from queue import Queue


queue_resource = Queue()

condition = threading.Condition(lock=threading.Lock())

def producer() -> None:	

	for i in range(2):

		sleep(3)

		condition.acquire()

		resource: str = f'resource_{randint(0, 10)}'

		queue_resource.put(resource)

		print(f'producer {threading.current_thread().name} -> {resource} produced')

		condition.notify()

		condition.release()


def consumer() -> None:

	condition.acquire()

	print(f'consumer {threading.current_thread().name} -> waiting resource')

	condition.wait()

	print(f'consumer {threading.current_thread().name} -> {queue_resource.get()} consumed')

	condition.release()


thread_producer = threading.Thread(name='thread_producer', target=producer)

thread_consumer_1 = threading.Thread(name='thread_consumer_1', target=consumer)

thread_consumer_2 = threading.Thread(name='thread_consumer_2', target=consumer)

thread_producer.start()

thread_consumer_1.start()

thread_consumer_2.start()
