import multiprocessing as mp
import itertools


QUEUE = mp.Queue()

class Routine(mp.Process):

	def __init__(self, number: int, *args, **kwargs):

		mp.Process.__init__(self, *args, **kwargs)

		self.number = number

	def target(self, number: int) -> int:

		return 2 * number

	def run(self):

		result = self.target(self.number)

		QUEUE.put(result)

def main() -> None:

	for i in range(5):

		routine = Routine(number=i)

		routine.start()

		routine.join()

	for _ in range(5):

		print(QUEUE.get())

if __name__ == '__main__':

	main()
