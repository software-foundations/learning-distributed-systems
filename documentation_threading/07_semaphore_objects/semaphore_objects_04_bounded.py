import threading
from time import sleep

N_MAX_CLIENTS_LOGGED_SIMULNANEOUSLY: int = 5

N_CLIENTS: int = 15

N_SEMAPHORE_RELEASE: int = 10 # only in python 3.9

semaphore = threading.BoundedSemaphore(value=N_MAX_CLIENTS_LOGGED_SIMULNANEOUSLY)

def client() -> None:

	semaphore.acquire()	

	print(f'\n{threading.current_thread().name} -> logged in -> N ACTIVED THREADS: {threading.active_count()}')		

	sleep(2)

	print(f'\n{threading.current_thread().name} -> logging out')	

	semaphore.release(n=N_MAX_CLIENTS_LOGGED_SIMULNANEOUSLY)

for i in range(N_CLIENTS):

	threading.Thread(name=f'client_{i}', target=client).start()

	if i == 4: 

		print('\nsleep\n')

		sleep(5)

"""
File "/usr/lib/python3.9/threading.py", line 504, in release
semaphore.release(n=N_MAX_CLIENTS_LOGGED_SIMULNANEOUSLY)raise ValueError("Semaphore released too many times")    
raise ValueError("Semaphore released too many times")

ValueError      File "/usr/lib/python3.9/threading.py", line 504, in release
ValueError: : Semaphore released too many times
"""