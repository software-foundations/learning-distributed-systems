#gather communication – Section 3: Process Based Parallelism
from mpi4py import MPI

# mpiexec -n 2 python gather.py

comm = MPI.COMM_WORLD
size = comm.Get_size() # num of cores
print(size)
rank = comm.Get_rank()
data = (rank+1)**2 # it will

print(f'data: {data}\nrank: {rank}')


data = comm.gather(data, root=0)
if rank == 0:
   print ("rank = %s " %rank +\
          "...receiving data to other process")
   print('>>>>>>> ', range(1,size)[-1]) # my modification
   for i in range(1,size):
   # ignores the core 0.
   # Test for i in range(1,size): print(i)  
      data[i] = (i+1)**2
      value = data[i]
      print(" process %s receiving %s from process %s"\
            %(rank , value , i))


"""
1. building the process data and send it to root processes

2. Collecting the data in an array
-------------
The gather function performs the inverse of
the scatter functionality

All processes send data to a root process that collects the data 
received

recvbuf = comm.gather(sendbuf, rank_of_root_process)
------------
Gatherering to one task: comm.Gather, comm.Gatherv, comm.gather

Gathering to all tasks: comm.Allgather, comm.Allgatherv, and 
comm.allgather
"""