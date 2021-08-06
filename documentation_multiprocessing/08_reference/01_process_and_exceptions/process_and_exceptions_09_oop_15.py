import multiprocessing as mp


class Routine(mp.Process):

	def __init__(self, *args, **kwargs):

		super(Routine, self).__init__(*args, **kwargs)

	def target(self):		

		print('pid after start: ', self.pid)

	def run(self):

		self.target()


def main():

	routine = Routine()

	print('pid before start: ', routine.pid)

	routine.start()	

	routine.join()

	print('joined')

	print('pid after join: ', routine.pid)

if __name__ == '__main__':

	main()
