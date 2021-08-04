from multiprocessing import Process
import os


def target_function() -> None:

	print(f'\niteration {os.getpid()}')	

def main() -> None:

	for i in range(100):

		# The constructor should always be called with keyword arguments. group 
		# should always be None

		process = Process(
			target=target_function)

		process.start()

if __name__ == '__main__':

	main()
