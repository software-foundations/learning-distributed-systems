import multiprocessing as mp
import os

class Routine(mp.Process):

	def __init__(self, *args, **kwargs):

		mp.Process.__init__(self, *args, **kwargs)

	def f(self) -> None:

		print(f'\nhello process {mp.current_process().name}, from {os.getppid()} parent process')

	def run(self) -> None:

		self.f()

def main() -> None:

	print(f'main process: {os.getpid()}')

	for i in range(100):

		routine = Routine(name=f'{i}')

		routine.start()

if __name__ == '__main__':

	main()
