import threading


N_ITERATIONS: int = 3

rlock = threading.RLock()

resource: list = []

def target_function(n_iterations: int = 5):

	current_thread: threading.Thread = threading.current_thread()

	thread_name: str = current_thread.name

	is_alive: bool = current_thread.is_alive()

	print(f'\n{thread_name} -> is_alive: {is_alive}')

	rlock.acquire()

	print(f'\n{thread_name} -> aquire OUTER rlock')

	for i in range(n_iterations):

		resource.append(thread_name + '_i_' + str(i))

		rlock.acquire()

		print(f'\n\t{thread_name} -> aquire INNER rlock')

		for j in range(n_iterations):

			resource.append(thread_name + '_j_' + str(j))

		rlock.release()

		print(f'\n\t{thread_name} -> release INNER rlock')	

	print(f'\n{thread_name} -> release OUTER rlock')

	print(f"\n{30 * '#'}")

	print(f'{thread_name} release resource: {resource}')

	rlock.release()


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
