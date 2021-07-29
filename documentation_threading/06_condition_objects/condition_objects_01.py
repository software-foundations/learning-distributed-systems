import threading 
from random import randint
from queue import Queue


queue_resource = Queue()

condition = threading.Condition(lock=threading.Lock())

def producer() -> None:	

	condition.acquire()

	resource: str = f'resource_{randint(0, 10)}'

	queue_resource.put(resource)

	print(f'producer -> {resource} produced')

	condition.notify()

	condition.release()


def consumer() -> None:

	condition.acquire()

	print('consumer -> waiting resource')

	condition.wait()

	print(f'consumer -> {queue_resource.get()} consumed')


thread_producer = threading.Thread(name='thread_producer', target=producer)

thread_consumer = threading.Thread(name='thread_consumer', target=consumer)

thread_consumer.start()

thread_producer.start()
