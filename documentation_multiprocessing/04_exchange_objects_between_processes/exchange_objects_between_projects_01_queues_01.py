from multiprocessing import Process, Queue


def target_function(queue: Queue) -> None:

	queue.put([20, None, 'hello'])

if __name__ == '__main__':

	# The Queue class is a near clone of queue.Queue
	
	# Queues are thread and process safe.
	
	queue = Queue()

	process = Process(name='process_01', target=target_function, args=(queue,))

	process.start()

	print(queue.get())

	process.join()

	print(f'{process.name} joined')
