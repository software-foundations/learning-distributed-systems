import multiprocessing as mp
from time import sleep
from random import randint


class Routine(mp.Process):

	def run(self) -> None:

		print(f'\nhello {mp.current_process().name}')

		sleep(randint(0, 10))

		self.target()

	def target(self) -> None:

		print(f'\nprocess {mp.current_process().name} executed')

def main() -> None:

	for i in range(100):

		routine = Routine(name=f'process {i}')

		routine.start()

if __name__ == '__main__':

	main()
