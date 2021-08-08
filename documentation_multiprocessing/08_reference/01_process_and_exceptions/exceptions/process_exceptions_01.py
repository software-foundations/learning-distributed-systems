'''
exception multiprocessing.ProcessError
	The base class of all multiprocessing exceptions.

exception multiprocessing.BufferTooShort
	Exception raised by Connection.recv_bytes_into() when the supplied buffer 
	object is too small for the message read.

	If e is an instance of BufferTooShort then e.args[0] will give 
	the message as a byte string.

exception multiprocessing.AuthenticationError
	Raised when there is an authentication error.

exception multiprocessing.TimeoutError
	Raised by methods with a timeout when the timeout expires.
'''