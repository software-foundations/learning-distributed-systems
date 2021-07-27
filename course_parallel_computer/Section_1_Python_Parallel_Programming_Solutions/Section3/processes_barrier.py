#Synchronize processes with barrier – Chapter 3: Process Based Parallelism

import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

"""
importante

Primitivas de sincronização

1. Lock -> aquire() and release()

2. Event -> set() and clear()

3. Condition -> wait() and notify_all()

4. Semafore -> used to share a common resource

5. RLock -> this defines a recursive lock object

6. Barries -> this divides a program into phases
"""

"""
Basicamente, uma barreira é criada. O primeiro processo que chega na barreira executa, toma posse da trava, executa, terminar de executar e então sinaliza o processo que está aguardando. O processo que estava aguardando então é executado
"""
"""
Barrier Objects

This class provides a simple synchronization primitive for use by a fixed number of threads that need to wait for each other. Each of the threads tries to pass the barrier by calling the wait() method and will block until all of the threads have made their wait() calls. At this point, the threads are released simultaneously.

The barrier can be reused any number of times for the same number of threads.
"""
"""
Então na verdade, barrier bloqueia a thread do processo, e não o processo em si. Como estamos, nesse exemplo, trabalhando com processo monothread, então o processo como um todo é bloqueado.
"""
def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait() # to wait the process at ther barrier ends
    now = time()
    with serializer: # using a Lock (serializer) with context manager (with)
        print("process %s ----> %s" \
              %(name,datetime.fromtimestamp(now)))

def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" \
          %(name ,datetime.fromtimestamp(now)))

if __name__ == '__main__':
    synchronizer = Barrier(2) # test with 1 and 2! 
    serializer = Lock()
    Process(name='p1 - test_with_barrier'\
            ,target=test_with_barrier,\
            args=(synchronizer,serializer)).start()
    Process(name='p2 - test_with_barrier'\
            ,target=test_with_barrier,\
            args=(synchronizer,serializer)).start()
    Process(name='p3 - test_without_barrier'\
            ,target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier'\
            ,target=test_without_barrier).start()
    

"""
output

process p2 - test_with_barrier ----> 2020-12-24 05:09:09.099636
process p1 - test_with_barrier ----> 2020-12-24 05:09:09.099678
process p3 - test_without_barrier ----> 2020-12-24 05:09:09.100225
process p4 - test_without_barrier ----> 2020-12-24 05:09:09.101305
"""

"""
1. p1 chega na barreira de 2
2. p1 espera chegar mais um processo, pois só há 1 processo na barreira de 2
3. p2 chega na barreira de 2
4. p2 sinaliza para p1 que já executar, pois já existem 2 processos na barreira de 2.
5. p1 e p2 são executados em paralelo
6. p2 executa ligeiramente primeiro que p1, pois p2 foi o processo que liberou a execução de p1. Logo, faz sentido que p1 execute primeiro

(pode ocorrer de p3 ou p4 executarem antes de p1)

7. p3 e p4 são executados em paralelo
"""

"""
pode ocorrer ...

process p2 - test_with_barrier ----> 2020-12-24 05:25:11.533945
process p3 - test_without_barrier ----> 2020-12-24 05:25:11.533951
process p1 - test_with_barrier ----> 2020-12-24 05:25:11.533986
process p4 - test_without_barrier ----> 2020-12-24 05:25:11.536086
"""