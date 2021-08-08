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

connection_1, connection_2 = mp.Pipe()

obj_to_send: object = 'hello'

connection_1.send(obj=obj_to_send)

obj_received = connection_2.recv()

print(obj_received)
