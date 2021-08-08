"""
Returns a process shared queue implemented using a pipe and a few locks/
semaphores. When a process first puts an item on the queue a feeder thread is 
started which transfers objects from a buffer into the pipe.

The usual queue.Empty and queue.Full exceptions from the standard 
library’s queue 
module are raised to signal timeouts.

Queue implements all the methods of queue.Queue except 
for task_done() and join().
"""

"""
qsize()
	Return the approximate size of the queue. Because of multithreading/
	multiprocessing semantics, this number is not reliable.

	Note that this may raise NotImplementedError on Unix platforms like Mac OS X 
	where sem_getvalue() is not implemented.
"""

import multiprocessing as mp


QUEUE = mp.Queue()

print(QUEUE.qsize())
