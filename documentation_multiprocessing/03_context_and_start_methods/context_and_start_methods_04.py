import multiprocessing as mp
import os
from random import choice
from typing import Union, NewType


NUMBER_PROCESSES: int = 10

Context = NewType('Context', Union[
	mp.context.ForkContext, 
	mp.context.SpawnContext, 
	mp.context.ForkServerContext])

def create_randomly_context_to_create_process() -> Context:

	def sort_method() -> str:

		return choice(['spawn', 'fork', 'forkserver'])

	return mp.get_context(method=sort_method())

def processes_info() -> None:

	print(f'\n\tprocess id \t\t-> {os.getpid()}')

	print(f'\n\tparent process id \t-> {os.getppid()}')

def target_function(queue: mp.Queue, item: int) -> None:	

	processes_info()

	queue.put(item)

	print(f'\n\tput item {item}')

if __name__ == '__main__':

	print(f'\n\n\n MAIN PROCESS: {os.getpid()}')

	# get_context should not be used more than once in the program.

	context = create_randomly_context_to_create_process()

	queue = mp.Queue()	

	for i in range(NUMBER_PROCESSES):

		process = context.Process(
			name=f'{context.__class__} ppid={os.getpid()}', 
			target=target_function,
			args=(queue, i,))

		print(f'\n-> process name: {process.name}')

		process.start()

		process.join()

		print(f'\n{process.name} joined')

		print(f'\nqueue.get {queue.get()}')
