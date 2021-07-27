#scatter communication – Section 3: Process Based Parallelism
from mpi4py import MPI

"""
mpiexec -n 2 python scatter.py
"""
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print(comm.Get_size()) # i believe that it return the number of cores

# if rank == 1: # try this to evaulate the error
if rank == 0:
   # array_to_share = [1, 2, 3, 4 ,5 ,6 ,7, 8 ,9 ,10] # it doesn't' work because my computer has only two cores
   array_to_share = [10, 4]

else:
   array_to_share = None

recvbuf = comm.scatter(array_to_share, root=0)
print("process = %d" %rank + " variable shared  = %d " %recvbuf )

"""
output:

process = 0 variable shared  = 10 
process = 1 variable shared  = 4
"""
"""
1. The process 0 create the array to be shared
2. The process 0 get the element at the position 0 (10) in the array
3. The process 1 get the element at the position 1 (4) in the array
"""

"""
The scatter functionality is very similar to a scatter broadcast



The difference is that comm.bcast sends the same

data to all listening processes and comm.scatter can

send the chunks of data in an array to different processes
"""

"""
Documentation

Collective calls like scatter(), gather(), allgather(), alltoall() 
expect a single value or a sequence of Comm.size elements at the root 
or all process. They return a single value, a list of Comm.size 
elements, or None.

Communication of buffer-like objects

You have to use method names starting with an upper-case letter (of the
 Comm class), like Send(), Recv(), Bcast(), Scatter(), Gather().

In general, buffer arguments to these calls must be explicitly specified
 by using a 2/3-list/tuple like [data, MPI.DOUBLE], or [data, count, MPI.DOUBLE] (the former one uses the byte-size of data and the extent 
 of the MPI datatype to define count).

For vector collectives communication operations like Scatterv() and Gatherv(), buffer arguments are specified 
as [data, count, displ, datatype], where count and displ are sequences 
of integral values.
"""