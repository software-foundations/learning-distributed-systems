import threading

def target_function() -> None:
	print('threading.current_thread().is_alive(): ', threading.current_thread().is_alive())

thread_01 = threading.Thread(target=target_function)

print('thread_01.is_alive(): ', thread_01.is_alive())

thread_01.start()

