from mpi4py import MPI

comm=MPI.COMM_WORLD
rank = comm.rank
print("my rank is : " , rank)

"""
mpiexec -n 2 python deadLockProblems.py
"""

"""
A deadlock is a situation where two (or more) process block each other
and wait for the other perform a certain action that servers to another, and vice versa.

The mpi4py module doesn't provide any specifc functionality to resolve this
but only some measures, which the developer must follow to avoid problems of deadolock
"""

"""
sendrecv() avoid deadLockProblem by processes interlocking each other
that will share data bidirectionaly
"""

"""
In MPI for Python, the MPI.Comm.Send(), MPI.Comm.Recv() and MPI.Comm.Sendrecv()
methods of communicator objects provide support for blocking point-to-point 
communications within MPI.Intracomm and MPI.Intercomm instances. 
These methods can communicate memory buffers. The variants MPI.Comm.send(), 
MPI.Comm.recv() and MPI.Comm.sendrecv() can communicate general Python objects.
"""

if rank == 0:
    data_send = "a"
    destination_process = 1 # the process which this one will send (dest) data
    source_process = 1 # the process which this one will receive (source) data

    print('process {} ready to sendrecv()'.format(rank)) # my modification
    data_received = comm.sendrecv(data_send, dest=destination_process, source=source_process)
    print('process {} sendrecv() is OK. DATA RECEIVED'.format(rank)) # my modification

    print ("sending data %s " %data_send + \
       "to process %d" %destination_process)
    print ("data received is = %s" %data_received)



if rank==1:
    data_send= "b"
    destination_process = 0
    source_process = 0

    print('process {} ready to sendrecv()'.format(rank)) # my modification
    data_received=comm.sendrecv(data_send,dest=destination_process,source=source_process)
    print('process {} sendrecv() is OK. DATA RECEIVED'.format(rank)) # my modification


    print ("sending data %s :" %data_send + \
            "to process %d" %destination_process)
    print ("data received is = %s" %data_received)
