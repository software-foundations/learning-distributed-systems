from multiprocessing import Pool, TimeoutError
import time
import os


def target_function(number: float) -> None:

	return number * number

if __name__ == '__main__':
	
	with Pool(processes=4) as pool:

		print(pool.map(func=target_function, iterable=range(10)))

		for i in pool.imap_unordered(func=target_function, iterable=range(10)):

			print(i)

		###################################		
		# evaluate "f(20)" asynchronously #
		###################################

		# runs in *only* one process
		response = pool.apply_async(func=target_function, args=(20,))

		print(response.get(timeout=1))

		#########################################
		# evaluate "os.getpid()" asynchronously #
		#########################################

		# runs in *only* one process
		response = pool.apply_async(func=os.getpid, args=())

		# prints the PID of that process
		print(response.get(timeout=1))

		##########################################################################
		# launching multiple evaluations asynchronously *may* use more processes #
		##########################################################################

		multiple_results = [pool.apply_async(func=os.getpid, args=()) for i in range(4)]

		print([response.get(timeout=1) for response in multiple_results])

		##########################################
		# make a single worker sleep for 10 secs #
		##########################################

		response = pool.apply_async(time.sleep, (10,))

		try:

			print(response.get(timeout=1))

		except TimeoutError:

			print("We lacked patience and got a multiprocessing.TimeoutError")

		print("For the moment, the pool remains available for more work")

	# exiting the 'with'-block has stopped the pool
	print("Now the pool is closed and no longer available")
