from multiprocessing import Process, Value, Array
from typing import Iterable

# Data can be stored in a shared memory map using Value or Array. For example, the following code

# The 'd' and 'i' arguments used when creating num and arr are typecodes of 
# the kind used by the array module: 'd' indicates a double precision float 

# and 'i' indicates a signed integer.

# These shared objects will be process and thread-safe.

# For more flexibility in using shared memory one can use the
# multiprocessing.sharedctypes module which supports the creation of arbitrary 
# ctypes objects allocated from shared memory.

def target_function(shared_num: float, shared_array: Iterable):

	shared_num.value = 3.1415927

	for i in range(len(shared_array)):

		shared_array[i] = -shared_array[i]


if __name__ == '__main__':

	shared_num = Value('d', 0.0)

	shared_array = Array('i', range(0, 10))

	process = Process(target=target_function, args=(shared_num, shared_array))

	process.start()

	process.join()

	print(shared_num.value)	

	print(shared_array[:])
