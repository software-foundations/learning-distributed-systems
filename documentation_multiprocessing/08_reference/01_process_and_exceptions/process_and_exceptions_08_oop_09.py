import multiprocessing as mp
from time import sleep
import os


class Routine(mp.Process):

	def __init__(self, *args, **kwargs):

		mp.Process.__init__(self, *args, **kwargs)

	def f(self) -> None:

		print(f'\nhello process {mp.current_process().name}, from {os.getppid()} parent process. alive: {self.is_alive()}')

	def run(self) -> None:

		sleep(1)

		self.f()

def main() -> None:

	print(f'main process: {os.getpid()}')

	for i in range(10):

		routine = Routine(name=f'{i}')

		routine.start()		

		routine.join()

		print(f'process {routine.name} joined. is alive? {routine.is_alive()}')

if __name__ == '__main__':

	main()
