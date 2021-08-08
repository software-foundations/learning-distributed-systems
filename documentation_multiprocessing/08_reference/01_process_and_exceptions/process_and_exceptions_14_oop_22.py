import multiprocessing as mp
from time import sleep


class Routine(mp.Process):

	def __init__(self, *args, **kwargs):

		super(Routine, self).__init__(*args, **kwargs)

	def target(self) -> None:		

		print(f'\n{mp.current_process().name}: ')

		sleep(5)

	def run(self) -> None:

		self.target()

def main():

	routine = Routine()

	routine.start()

	routine.join(timeout=2)

	routine.kill()

if __name__ == '__main__':

	main()
