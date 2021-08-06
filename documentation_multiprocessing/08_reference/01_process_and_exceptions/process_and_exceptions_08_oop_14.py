import multiprocessing as mp


class Routine(mp.Process):

	def __init__(self, *args, **kwargs):

		mp.Process.__init__(self, *args, **kwargs)

	def target(self):

		print(f'\nhello process {mp.current_process().name}')

	def run(self):		

			self.target()

def main() -> None:

	NUMBER_OF_PROCESSES: int = 10

	for i in range(NUMBER_OF_PROCESSES):

		routine = Routine(daemon=True)

		routine.start()

		routine.join()

	print('All deamons executed')

if __name__ == '__main__':

	main()
