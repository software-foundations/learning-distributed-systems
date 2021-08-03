from multiprocessing import Manager, Process


# A manager object returned by Manager() controls a server process which holds 
# Python objects and allows other processes to manipulate them using proxies.

# A manager returned by Manager() will support types list, dict, Namespace, 
# Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, 
# Value and Array. For example,

# Server process managers are more flexible than using shared memory objects 
# because they can be made to support arbitrary object types. Also, a single 
# manager can be shared by processes on different computers over a network. 
# They are, however, slower than using shared memory.

def target_function(shared_dict: dict, shared_list: list) -> None:

	shared_dict['1'] = 1

	shared_dict['2'] = 2

	shared_dict[0.25] = None

	shared_list.reverse()

if __name__ == '__main__':

	with Manager() as manager:

		manager_dict = manager.dict()

		manager_list = manager.list(range(10))

		process = Process(
			target=target_function, 
			args=(manager_dict, manager_list))

		process.start()

		process.join()

		print(manager_dict)

		print(manager_list)
