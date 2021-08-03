import multiprocessing as mp

from time import sleep


# The Pipe() function returns a pair of connection objects connected by a pipe 
# which by default is duplex (two-way)

def target_function(connection) -> None:

	sleep(2)

	connection.send([20, None, 'hello'])

	sleep(2)


if __name__ == '__main__':

	parent_connection, child_connection = mp.Pipe()

	process = mp.Process(target=target_function, args=(child_connection,))

	process.start()

	print('parent_connection.recv() -> ', parent_connection.recv())

	process.join()

	print('Joined')
