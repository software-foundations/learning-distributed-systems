import threading
from time import sleep

TIMER_INTERVAL_SECONDS: int = 2

TIMEOUT_CANCEL_TIMER: float = 1

def target_function() -> None:

	print('Timer reached')

timer = threading.Timer(interval=TIMER_INTERVAL_SECONDS, function=target_function)

timer.start()

sleep(TIMEOUT_CANCEL_TIMER)

timer.cancel()

if TIMEOUT_CANCEL_TIMER < TIMER_INTERVAL_SECONDS:

	print('Timer canceled')

else:

	print('Timer not canceled')
