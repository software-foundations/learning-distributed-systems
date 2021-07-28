import threading
from time import sleep
from tqdm import tqdm


lock = threading.Lock()

resource: list = []


def target_function():

	current_thread: threading.Thread = threading.current_thread()

	thread_name: str = current_thread.name

	print(f'\n{thread_name} -> is_alive: {current_thread.is_alive()}')

	if lock.locked():

		print(f'\n{thread_name} -> waiting the source be avaliable')

	lock.acquire()

	print(f'\n{thread_name} -> acessing resource')

	for i in tqdm(range(3)):

		resource.append(i)

		sleep(1)

	print(resource)

	print(f'{thread_name} -> releasing resource')

	lock.release()
	
		
thread_01 = threading.Thread(name='t1', target=target_function)

thread_02 = threading.Thread(name='t2', target=target_function)

thread_01.start()

thread_02.start()