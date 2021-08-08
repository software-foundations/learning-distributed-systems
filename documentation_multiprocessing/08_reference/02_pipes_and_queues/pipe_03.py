"""
For passing messages one can use Pipe() (for a connection between two processes) 
or a queue (which allows multiple producers and consumers).

Returns a pair (conn1, conn2) of Connection objects representing the ends of a 
pipe.

If duplex is True (the default) then the pipe is bidirectional. If duplex is 
False then the pipe is unidirectional: conn1 can only be used for receiving 
messages and conn2 can only be used for sending messages.
"""

import multiprocessing as mp


receiver, sender = mp.Pipe(duplex=False)

obj_to_send: object = 'hello'

try:

	receiver.send(obj=obj_to_send)

	print(sender.recv())

except OSError:

	print('receiver cannot send objects. It can only receive')

sender.send(obj=obj_to_send)

print(receiver.recv())
