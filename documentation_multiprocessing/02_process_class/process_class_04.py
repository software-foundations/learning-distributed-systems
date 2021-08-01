from multiprocessing import Process
from time import sleep


def target_function(name: str) -> None:

	print(f'Hi -> {name}')

	sleep(2)

if __name__ == '__main__':
	
	process = Process(target=target_function, kwargs={'name': 'Bruno'})

	process.start()

	process.join()

	print('Process joined')
