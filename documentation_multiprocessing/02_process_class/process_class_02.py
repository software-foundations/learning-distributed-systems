from multiprocessing import Process
from time import sleep
from random import randint


def target_function() -> None:

	print(f'Hi -> {randint(0, 100)}')

	sleep(2)

if __name__ == '__main__':
	
	process = Process(target=target_function)

	process.start()

	process.join()

	print('Process joined')
