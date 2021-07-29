import threading
from tqdm import trange
from time import sleep

# TIMEOUT_LOCK: float = 4
TIMEOUT_LOCK: float = 0.5

lock = threading.Lock()

resource: list = []


def target_function():

	current_thread: threading.Thread = threading.current_thread()

	thread_name: str = current_thread.name

	print(f'\n{thread_name} -> is_alive: {current_thread.is_alive()}')

	if lock.locked():

		print(f'\n{thread_name} -> waiting the source be avaliable')

	lock.acquire(timeout=TIMEOUT_LOCK)

	print(f'\n{thread_name} -> aquire the lock')

	print(f'\n{thread_name} -> acessing resource')

	for i in trange(3):

		resource.append(str(i) + '_' + thread_name)

		sleep(1)

	print(resource)

	print(f'\n{thread_name} -> releasing resource')

	try:
		lock.release()

	except RuntimeError as e:
		print(thread_name, e, '-> invoked on an unlocked lock')
		print('ignored!')
	
		
thread_01 = threading.Thread(name='t1', target=target_function)

thread_02 = threading.Thread(name='t2', target=target_function)

thread_01.start()

thread_02.start()
