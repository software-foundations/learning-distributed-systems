import threading

counter_buffer = 0
counter_lock = threading.Lock()

COUNTER_MAX = 100

def counsumer1_counter():
	global counter_buffer
	for i in range(COUNTER_MAX):
		counter_lock.acquire()
		print(threading.current_thread().name, i)		
		counter_buffer += 1
		counter_lock.release()

def counsumer2_counter():
	global counter_buffer
	for i in range(COUNTER_MAX):		
		counter_lock.acquire()
		print(threading.current_thread().name, i)
		counter_buffer += 1
		counter_lock.release()


t1 = threading.Thread(target=counsumer1_counter, name='consumer1')
t2 = threading.Thread(target=counsumer2_counter, name='consumer2')

t1.start()
t2.start()

t1.join()
t2.join()

print(COUNTER_MAX)
