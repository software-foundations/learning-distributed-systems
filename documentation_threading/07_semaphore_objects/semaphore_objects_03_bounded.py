import threading
from time import sleep

N_MAX_CLIENTS_LOGGED_SIMULNANEOUSLY: int = 3

N_CLIENTS: int = 15

TIMEOUT_SEMAPHORE_ACQUIRE: float = 0.1

semaphore = threading.BoundedSemaphore(value=N_MAX_CLIENTS_LOGGED_SIMULNANEOUSLY)

def client() -> None:

	semaphore.acquire(timeout=TIMEOUT_SEMAPHORE_ACQUIRE)

	print(f'\n{threading.current_thread().name} -> logged in -> N ACTIVED THREADS: {threading.active_count()}')	

	sleep(3)

	print(f'\n{threading.current_thread().name} -> logging out')

	sleep(1)

	semaphore.release(n=TIMEOUT_SEMAPHORE_ACQUIRE)

for i in range(N_CLIENTS):

	threading.Thread(name=f'client_{i}', target=client).start()

"""
ValueError
:     ValueError:     : n must be one or moresemaphore.release(n=TIMEOUT_SEMAPHORE_ACQUIRE)
  File "/usr/lib/python3.9/threading.py", line 501, in release
      File "/usr/lib/python3.9/threading.py", line 501, in release
    n must be one or more
raise ValueError('n must be one or more')
ValueError: n must be one or more
"""