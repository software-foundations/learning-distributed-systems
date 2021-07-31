import threading
from time import sleep

N_MAX_CLIENTS_LOGGED_SIMULNANEOUSLY: int = 3

N_CLIENTS: int = 15

semaphore = threading.BoundedSemaphore(value=N_MAX_CLIENTS_LOGGED_SIMULNANEOUSLY)

def client() -> None:

	semaphore.acquire(blocking=False)

	print(f'\n{threading.current_thread().name} -> logged in -> N ACTIVED THREADS: {threading.active_count()}')	

	sleep(3)

	print(f'\n{threading.current_thread().name} -> logging out')

	sleep(1)

	semaphore.release()

for i in range(N_CLIENTS):

	threading.Thread(name=f'client_{i}', target=client).start()

"""
semaphore.release()

  File "/usr/lib/python3.9/threading.py", line 504, in release
    raise ValueError("Semaphore released too many times")
ValueError: Semaphore released too many times
"""