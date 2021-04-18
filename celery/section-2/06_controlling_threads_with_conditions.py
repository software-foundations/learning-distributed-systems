import threading

import time
import random

queue = []
MAX_ITEMS = 10

condition = threading.Condition()

class ProducerThread(threading.Thread):

	def run(self):

		numbers = range(5)
		global queue

		while True:
			condition.acquire()
			if len(queue) == MAX_ITEMS:
				print("Quere is full, producer is waiting")
				condition.wait()
				print("Space in quere, Consumer notified producer")
			number = random.choice(numbers)
			queue.append(number)
			print("Producer {}".format(number))
			condition.notify()
			condition.release()
			time.sleep(random.random())


class ConsumerThread(threading.Thread):

	def run(self):
		global queue
		while True:
			condition.acquire()
			if not queue:
				print("Nothing in queue, consumer is waiting")
				condition.wait()
				print("Producer added something to quere and notify the consumer")

			number = queue.pop(0)
			print("Consumer {}".format(number))
			condition.notify()
			condition.release()
			time.sleep(random.random())


producer = ProducerThread()
producer.start()

consumer = ConsumerThread()
consumer.start()
