import threading


TIMER_INTERVAL_SECONDS: int = 2

def target_function(name: str) -> None:

	print(f'{name}, Timer reached!')

timer = threading.Timer(
	interval=TIMER_INTERVAL_SECONDS, 
	function=target_function,
	args=('Bruno',))

timer.start()
