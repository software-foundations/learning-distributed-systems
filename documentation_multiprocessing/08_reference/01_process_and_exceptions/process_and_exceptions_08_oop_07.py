import multiprocessing as mp
import os


class Routine(mp.Process):

	def __init__(self, *args, **kwargs):

		mp.Process.__init__(self, *args, **kwargs)

	def f(self) -> None:

		print(f'\nhello process {os.getpid()}, from {os.getppid()} parent process')

	def run(self) -> None:

		self.f()

def main() -> None:

	print(f'main process: {os.getpid()}')

	for _ in range(100):

		routine = Routine()

		routine.start()

if __name__ == '__main__':

	main()
