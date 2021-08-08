import multiprocessing as mp
from time import sleep


class Routine(mp.Process):

	def __init__(self, *args, **kwargs):

		super(Routine, self).__init__(*args, **kwargs)

	def target(self) -> None:		

		print(f'\n{mp.current_process().name}: ')

		sleep(4)

	def run(self) -> None:

		self.target()

def main():

	routine = Routine()

	routine.start()

	routine.join(timeout=2)

	routine.close()

	# ValueError: Cannot close a process while it is still running. 
	# You should first call join() or terminate().


if __name__ == '__main__':

	main()

# Note that the start(), join(), is_alive(), terminate() and exitcode methods
# should only be called by the process that created the process object.