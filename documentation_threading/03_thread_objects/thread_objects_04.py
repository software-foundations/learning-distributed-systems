import threading
from time import sleep
from tqdm import tqdm

TIMEOUT_JOIN_THREAD: float = 2

def target_function(seconds_to_sleep: int = 3) -> None:

	current_thread: threading.Thread = threading.current_thread()

	is_alive: bool = current_thread.is_alive()

	is_deamon: bool = current_thread.daemon

	print('is_alive: ', is_alive)

	print('is_deamon: ', is_deamon)
	
	for i in tqdm(range(seconds_to_sleep)):

		sleep(1)			

thread_01 = threading.Thread(
	name='t1', 
	kwargs={'seconds_to_sleep': 10},
	target=target_function)

thread_01.start()

thread_01.join(timeout=TIMEOUT_JOIN_THREAD)

print(thread_01.is_alive())

print('thread 01 joined')