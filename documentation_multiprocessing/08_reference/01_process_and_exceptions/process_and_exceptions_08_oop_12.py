import multiprocessing as mp


QUEUE = mp.Queue()

class Routine(mp.Process):

	def __init__(self, number: int, queue: mp.Queue, *args, **kwargs):

		mp.Process.__init__(self, *args, **kwargs)

		self.number = number

		self.QUEUE = queue

	def target(self, number) -> int:

		return number ** 2
		
	def run(self):

		result = self.target(number=self.number)

		self.QUEUE.put(result)

def main() -> None:

	for i in range(5):

		routine = Routine(queue=QUEUE, number=i)

		routine.start()

		routine.join()

	for _ in range(5):

		result = QUEUE.get()

		print(result)

if __name__ == '__main__':

	main()
