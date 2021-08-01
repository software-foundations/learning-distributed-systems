import multiprocessing as mp
import os


def processes_info() -> None:

	print(f'\n\tprocess id \t\t-> {os.getpid()}')

	print(f'\n\tparent process id \t-> {os.getppid()}')

def target_function() -> None:	

	processes_info()

if __name__ == '__main__':	

	# should not be used more than once in the program.

	# I don't know the difference between force=True/False

	mp.set_start_method('forkserver', force=True) # always copy of the same parent process

	# mp.set_start_method('forkserver', force=False) # always copy of the same parent process

	for _ in range(10):

		process = mp.Process(
			name=f'forkserver ppid={os.getpid()}', 
			target=target_function)

		print(f'\n-> process name: {process.name}')

		process.start()	

		process.join()

		print(f'\n{process.name} joined')
