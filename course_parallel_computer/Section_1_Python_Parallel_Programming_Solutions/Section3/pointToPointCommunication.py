from mpi4py import MPI

comm=MPI.COMM_WORLD
rank = comm.rank
print("my rank is : " , rank) # rank is the process/core. 

"""
mpiexec -n 2 python pointToPointCommunication.py
"""

if rank==0:
    data= 10000000
    # destination_process = 4 # it will don't work 'cause my computer has only two cores
    destination_process = 1

    comm.send(data,dest=destination_process)
    print ("process 0 sent data %s " %data +\
           "to process %d" %destination_process)
"""   
if rank==1:
    destination_process = 8
    data= "hello"
    comm.send(data,dest=destination_process)
    print ("sending data %s :" %data + \
           "to process %d" %destination_process)
"""


# if rank==4:
if rank==1:
    source_process = 0
    data=comm.recv(source=source_process)    
    print (f"process {rank} received data=%s from process {source_process}" %data)

# it will dont work because my computer has only two cores 
"""    
if rank==8:
    data1=comm.recv(source=1)
    print ("data1 received is = %s" %data1)
"""