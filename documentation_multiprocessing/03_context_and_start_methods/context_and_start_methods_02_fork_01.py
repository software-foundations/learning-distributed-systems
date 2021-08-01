import multiprocessing as mp
import os


def processes_info() -> None:

	print(f'\nprocess id \t\t-> {os.getpid()}')

	print(f'\nparent process id \t-> {os.getppid()}')

def target_function() -> None:

	processes_info()

if __name__ == '__main__':

	# should not be used more than once in the program.

	mp.set_start_method('fork') # copy of parent process	

	process = mp.Process(name='fork process', target=target_function)

	process.start()	

	process.join()

	print(f'\n{process.name} joined')
