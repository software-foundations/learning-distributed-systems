import threading
from queue import Queue
from random import randint


resource_queue = Queue()

condition = threading.Condition(lock=None)


def producer() -> None:

    with condition:

        resource_item = f'resource_{randint(0, 10)}'

        resource_queue.put(resource_item)

        print(f'{threading.current_thread().name} -> {resource_item} produced')

        condition.notify()


def consumer() -> None:

    condition.acquire()

    condition.wait(timeout=2)

    print(f'{threading.current_thread().name} -> waiting')

    print(f'{threading.current_thread().name} -> {resource_queue.get()} consumed')


thread_producer = threading.Thread(name='t_producer', target=producer)

thread_consumer = threading.Thread(name='t_consumer', target=consumer)

thread_producer.start()

thread_consumer.start()