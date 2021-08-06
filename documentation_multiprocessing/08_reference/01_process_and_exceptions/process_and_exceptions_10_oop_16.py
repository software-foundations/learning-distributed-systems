import multiprocessing as mp


class Routine(mp.Process):

	def __init__(self, *args, **kwargs):

		super(Routine, self).__init__(*args, **kwargs)

	def target(self):		

		print('exitcode after start: ', self.exitcode)

	def run(self):

		self.target()

def main():

	routine = Routine()

	print('exitcode before start: ', routine.exitcode)

	routine.start()	

	routine.join()

	print('joined')	

	print('exitcode after join: ', routine.exitcode)

if __name__ == '__main__':

	main()
