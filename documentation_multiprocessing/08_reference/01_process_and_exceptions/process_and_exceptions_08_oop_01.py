import multiprocessing as mp


class Routine(mp.Process):

	def run(self):

		print(f'hello {mp.current_process().name}')

def main() -> None:

	for i in range(100):

		routine = Routine(name=f'process {i}')

		routine.start()

if __name__ == '__main__':

	main()