from multiprocessing import Lock, Process
import os
from time import sleep
from typing import NewType


Resource = NewType('Resource', list)

ResourceItem = NewType('ResourceItem', int)

ProcessLock = NewType('ProcessLock', Lock)

ProcessName = NewType('ProcessName', str)

def client(lock: ProcessLock, resource: Resource, resource_item: ResourceItem) -> None:

	try:
		
		lock.acquire()

		resource.append(resource_item)

		print(f'\nprocess {os.getpid()} -> resource added')

		sleep(1)

	finally:

		lock.release()

process = Process(target=client)

if __name__ == '__main__':

	LOCK = Lock()

	resource = []

	for resource_item in range(5):

		Process(target=client, args=(LOCK, resource, resource_item,)).start()
