import multiprocessing as mp


class Routine(mp.Process):

	def __init__(self, *args, **kwargs):

		super(Routine, self).__init__(*args, **kwargs)

	def target(self):		

		print('\nauthkey after start: ', self.authkey)

		is_authkey_child_equal_parent = self.check_child_authkey_equal_parent()

		is_changed_authkey_child_equal_parent = self.alter_child_authkey_and_check_equal_parent()

		print(f'\nauthkey child == parent : {is_authkey_child_equal_parent}')

		print(f'\nchanged authkey child == parent : {is_changed_authkey_child_equal_parent}')

	def check_child_authkey_equal_parent(self) -> bool:

		return Routine().authkey == self.authkey

	def alter_child_authkey_and_check_equal_parent(self) -> bool:

		child_routine = Routine()

		child_routine.authkey = b'my authkey'

		return self.authkey == child_routine.authkey

	def run(self):

		self.target()

def main():

	routine = Routine()

	print('\nauthkey before start: ', routine.authkey)

	routine.start()	

	routine.join()

	print('\njoined')	

	print('\nauthkey after join: ', routine.authkey)

if __name__ == '__main__':

	main()
