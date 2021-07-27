#broadcast communication Section 3: Process Based Parallelism
from mpi4py import MPI

"""
mpiexec -n 2 python broadcast.py 
"""
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# print(rank, comm.rank) # it show that comm.Get_rank and comm.rank are different methods to access the same rank attribute

if rank == 0:
   variable_to_share = 100

else:
   variable_to_share = None

# if not rank == 0: # it doesn't work
variable_to_share = comm.bcast(variable_to_share, root=0)
print("process = %d" %rank + " variable shared  = %d " %variable_to_share)

"""
 So, the first parameter is the data, the second, "root," means "from what node." With broadcast, all nodes automatically accept the data, under the data var name.
"""