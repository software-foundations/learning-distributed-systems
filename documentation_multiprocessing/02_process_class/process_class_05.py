from multiprocessing import Process
import os


def processes_info() -> None:

	print(f'Process id \t\t -> {os.getpid()}')

	print(f'Parent Process id \t -> {os.getppid()}')

def target_function() -> None:	

	print(f'module name: ', __name__)

	processes_info()	

if __name__ == '__main__':

	process = Process(target=target_function)

	process.start()
