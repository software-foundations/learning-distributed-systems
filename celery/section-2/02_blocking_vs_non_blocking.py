import time
import threading


def countdown(count):
	while(count >= 0):
		print("{} {}".format(threading.current_thread().name, count))
		count -= 1
		time.sleep(2)


def countup(count):
	while(count <= 10):
		print("{} {}".format(threading.current_thread().name, count))
		count += 1
		time.sleep(2)

t1 = threading.Thread(name='countdown', args=(10,), target=countdown)
t1.start()

t2 = threading.Thread(name='countup', args=(0,), target=countup)
t2.start()

print("All done!")