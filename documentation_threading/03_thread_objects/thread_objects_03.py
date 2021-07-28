import threading


def target_function(person_01: str = 'p1', person_02: str = 'p2') -> None:

	print(threading.current_thread().name)

	print(threading.current_thread().is_alive())

	print(f'person_01: {person_01}')

	print(f'person_02: {person_02}')
		

thread_01 = threading.Thread(
	# name='t1', 
	target=target_function, 
	kwargs={'person_01': 'Bruno', 'person_02': 'Hanna'})

thread_01.start()

thread_01.join()

print('executed after join thread 01')
