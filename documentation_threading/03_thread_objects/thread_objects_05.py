import threading
from time import sleep
from tqdm import tqdm

def target_function(sleep_time: int = 5):

	print('is_deamon: ', threading.current_thread().isDaemon())
	
	for _ in tqdm(range(sleep_time)):

		sleep(1)


thread_01 = threading.Thread(name='t1', target=target_function, args=[2], daemon=True)

# thread_01.daemon = False

thread_01.start()

thread_01.join()

print('thread_01 joined')
