#Synchronize processes with managers – Section 3: Process Based Parallelism
import multiprocessing

"""
Managers

Managers provide a way to create data which can be shared between different processes, including sharing over a network between processes running on different machines. A manager object controls a server process which manages shared objects. Other processes can access the shared objects by using proxies.

multiprocessing.Manager()
Returns a started SyncManager object which can be used for sharing objects between processes. The returned manager object corresponds to a spawned child process and has methods which will create shared objects and return corresponding proxies.

Manager processes will be shutdown as soon as they are garbage collected or their parent process exits. The manager classes are defined in the multiprocessing.managers module:
"""
def worker(dictionary, key, item):
    dictionary[key] = item

if __name__ == '__main__':
    mgr = multiprocessing.Manager()    
    dictionary = mgr.dict() # assim funciona
    # dictionary = {} # assim nao funciona
    jobs = [ multiprocessing.Process\
             (target=worker, args=(dictionary, i, i*2))
             for i in range(10)
             ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print ('Results:', dictionary)
