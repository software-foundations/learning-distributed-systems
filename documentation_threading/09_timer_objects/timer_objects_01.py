import threading
from time import sleep

TIMER_INTERVAL_SECONDS: int = 2

def target_function() -> None:

	print('Timer reached')

timer = threading.Timer(interval=TIMER_INTERVAL_SECONDS, function=target_function)

timer.start()
