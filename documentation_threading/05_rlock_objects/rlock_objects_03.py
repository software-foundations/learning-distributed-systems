import threading

from time import sleep

N_ITERATIONS: int = 1

TIMEOUT_RLOCK: float = 4.0

rlock = threading.RLock()

resource: list = []

def target_function(n_iterations: int = 5):

	current_thread: threading.Thread = threading.current_thread()

	thread_name: str = current_thread.name

	is_alive: bool = current_thread.is_alive()

	print(f'\n{thread_name} -> is_alive: {is_alive}')

	try:

		rlock.acquire(blocking=False)

	except RuntimeError as e:

		print(thread_name, e)

	print(f'\n{thread_name} -> aquire OUTER rlock')

	for i in range(n_iterations):

		resource.append(thread_name + '_i_' + str(i))

		rlock.acquire(blocking=True, timeout=TIMEOUT_RLOCK)

		print(f'\n\t{thread_name} -> aquire INNER rlock')

		for j in range(n_iterations):

			resource.append(thread_name + '_j_' + str(j))

			sleep(1)

		rlock.release()

		print(f'\n\t{thread_name} -> release INNER rlock')	

	print(f'\n{thread_name} -> release OUTER rlock')

	print(f"\n{30 * '#'}")

	print(f'{thread_name} release resource: {resource}')

	try:

		rlock.release()

	except RuntimeError as e:

		print(thread_name, e)


thread_01 = threading.Thread(
	name='t1', 
	target=target_function, 
	args=(N_ITERATIONS,))

thread_02 = threading.Thread(
	name='t2', 
	target=target_function, 
	args=(N_ITERATIONS,))

thread_01.start()

thread_02.start()
