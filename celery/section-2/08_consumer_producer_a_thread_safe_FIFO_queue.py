import threading

import time
import random

import queue

_queue = queue.Queue(10)

MAX_ITEMS = 10


class ProducerThread(threading.Thread):

	def run(self):

		numbers = range(5)
		global _queue

		while True:			
			number = random.choice(numbers)
			_queue.put(number)
			print("Producer {}".format(number))
			time.sleep(random.random())


class ConsumerThread(threading.Thread):

	def run(self):
		global _queue

		while True:				
			number = _queue.get()
			_queue.task_done()
			print("Consumed {}".format(number))
			time.sleep(random.random())


producer = ProducerThread()
producer.daemon = True
producer.start()

consumer = ConsumerThread()
consumer.daemon = True
consumer.start()

while True:
	time.sleep(1)