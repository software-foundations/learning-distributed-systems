import threading

TIMEOUT_EVENT: float = 4

event = threading.Event()

def target_wait_for_event() -> None:

	print(f'\n{threading.current_thread().name} -> waiting for the event')

	print('\nevent.is_set(): ', event.is_set())

	event.wait(timeout=TIMEOUT_EVENT)

	print(f'\n{threading.current_thread().name} -> event occurred or timeout is rached')

	print('\nevent.is_set(): ', event.is_set())

	event.clear()

	print('\nevent.clear()')

	print('\nevent.is_set()', event.is_set())

	print('\nevent.clear() -> can be possible to waiting for the event again')

def target_event() -> None:

	input(f'\n{threading.current_thread().name} ->Press something to clear the event')

	event.set()

	print(f'\n{threading.current_thread().name} -> event setted')	

thread_wait_for_event = threading.Thread(
	name='thread_wait_for_event',
	target=target_wait_for_event)

thread_event = threading.Thread(
	name='thread_event',
	target=target_event)


thread_event.start()
thread_wait_for_event.start()