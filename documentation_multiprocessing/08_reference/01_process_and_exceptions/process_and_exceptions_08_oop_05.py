import multiprocessing as mp
import os


class Routine(mp.Process):

	def __init__(self, *args, **kwargs):

		super(Routine, self).__init__(*args, **kwargs)

def f() -> None:

	print(f'\nhello process {os.getpid()}, from {os.getppid()} parent process')

def main() -> None:

	print(f'main process: {os.getpid()}')

	for _ in range(100):

		routine = Routine(target=f)

		routine.start()

if __name__ == '__main__':

	main()
