#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing

from os import cpu_count

print('n. processers: ', cpu_count()) # cpu_count() é o valor default do tamanho da piscina

"""
https://docs.python.org/3/library/multiprocessing.html

Process Pools
One can create a pool of processes which will carry out tasks submitted to it with the Pool class.

class multiprocessing.pool.Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])
A process pool object which controls a pool of worker processes to which jobs can be submitted. It supports asynchronous results with timeouts and callbacks and has a parallel map implementation.

processes is the number of worker processes to use. If processes is None then the number returned by os.cpu_count() is used.

If initializer is not None then each worker process will call initializer(*initargs) when it starts.

maxtasksperchild is the number of tasks a worker process can complete before it will exit and be replaced with a fresh worker process, to enable unused resources to be freed. The default maxtasksperchild is None, which means worker processes will live as long as the pool.

context can be used to specify the context used for starting the worker processes. Usually a pool is created using the function multiprocessing.Pool() or the Pool() method of a context object. In both cases context is set appropriately.

Note that the methods of the pool object should only be called by the process which created the pool.

Warning multiprocessing.pool objects have internal resources that need to be properly managed (like any other resource) by using the pool as a context manager or by calling close() and terminate() manually. Failure to do this can lead to the process hanging on finalization.
Note that is not correct to rely on the garbage colletor to destroy the pool as CPython does not assure that the finalizer of the pool will be called (see object.__del__() for more information).
"""

"""
apply(): it blocks until the result is ready

aaply_async(): it is an asynchronous operation that will not lock the main thread until all the child classes are executed

map(): It blocks until the result is ready, this method chops the iteraple data in a number of chunks that submits to the process pool as separate tasks

map_async(): This is a variant of the map method, wich returns a result object
"""
def function_square(data):
    result = data*data
    return result


if __name__ == '__main__':
    inputs = list(range(0,100))
    pool = multiprocessing.Pool(processes=4) # uma piscina de processos paralelos que comporta até 4 processos

    """way 1"""
    pool_outputs = pool.map(function_square, inputs)
    pool.close() # fecha cada um dos 4 processos da piscina
    pool.join()  # aguarda
    print ('Pool    :', pool_outputs)
    
    """way 2 - testar !"""
    # pool_obj = pool.map_async(function_square, inputs)    
    # print(pool_obj) # agora nao sei como utilizar esse objeto
