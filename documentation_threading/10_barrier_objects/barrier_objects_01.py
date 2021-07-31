import threading
from time import sleep


NUMBER_PARTIES: int = 2

NUMBER_TOTAL_OF_PEOPLE: int = 5

NUMPER_PEOPLE_LEFT: int = NUMBER_TOTAL_OF_PEOPLE % NUMBER_PARTIES

TIMEOUT_BARRIER_INTERVAL: float = 3

SLEEP_TIME_BETWEEN_RAISE_HANDS: float = 1

def touch_of_hands_of_two_people() -> None:

	list_threads_name: list = list(map(lambda t: t.name, threading.enumerate()))

	print(f'\n{list_threads_name} -> touch of hands')

barrier = threading.Barrier(
	parties=NUMBER_PARTIES, 
	action=touch_of_hands_of_two_people,
	timeout=TIMEOUT_BARRIER_INTERVAL)

def person() -> None:

	try:

		print(f'\n{threading.current_thread().name} -> raise my hand')

		barrier.wait()

	except threading.BrokenBarrierError:

		print(f'\n{threading.current_thread().name} -> 1 person is left to touch my hand')

for i in range(NUMBER_TOTAL_OF_PEOPLE):

	threading.Thread(name=f'thread_person_{i}', target=person).start()

	sleep(SLEEP_TIME_BETWEEN_RAISE_HANDS)
