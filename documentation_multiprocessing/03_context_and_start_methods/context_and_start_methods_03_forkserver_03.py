import multiprocessing as mp
import os


def processes_info() -> None:

	print(f'\n\tprocess id \t\t-> {os.getpid()}')

	print(f'\n\tparent process id \t-> {os.getppid()}')

def target_function() -> None:	

	processes_info()

if __name__ == '__main__':	

	# should not be used more than once in the program.

	context = mp.get_context(method='forkserver') # always copy of the same parent process	

	for _ in range(10):

		process = context.Process(
			name=f'forkserver ppid={os.getpid()}', 
			target=target_function)

		print(f'\n-> process name: {process.name}')

		process.start()	

		process.join()

		print(f'\n{process.name} joined')
