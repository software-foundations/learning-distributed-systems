import threading


def target_function(name: str = 'someone') -> None:
	print(f'hello, {name}!')
	print(f'you are in the thread {threading.current_thread().name}')


thread_01 = threading.Thread(name='t1', target=target_function, args=['Bruno'])

thread_01.start()

print('executed in an incertain monment (after or along thread exection)')

thread_01.join()

print('executed after join thread 01')