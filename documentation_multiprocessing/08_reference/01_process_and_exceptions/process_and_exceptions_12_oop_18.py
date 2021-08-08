import multiprocessing as mp
from time import sleep


class Routine(mp.Process):

	def __init__(self, *args, **kwargs):

		super(Routine, self).__init__(*args, **kwargs)

	def target(self) -> None:		

		print(f'\n{mp.current_process().name}: ')

		# sleep(10 * 6)

	def run(self) -> None:

		self.target()

def main():

	li_routines = [Routine() for _ in range(5)]

	[routine.start() for routine in li_routines]

	print([routine.sentinel for routine in li_routines])

	mp.connection.wait(object_list=li_routines)

	# AttributeError: module 'multiprocessing' has no attribute 'connection'

	print('ends')

if __name__ == '__main__':

	main()
