import threading
import logging

"""
Mostra que um lock pode ser adquirido usando with ao invés de usar lock.aquire()
Isso foi testado para lock, RLock, Semáforo, Condição e semáforo
"""
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

def threading_with(statement):
    with statement:
        logging.debug('%s acquired via with'  %statement)
        
def threading_not_with(statement):
    statement.acquire()
    try:
        logging.debug('%s acquired directly' %statement )
    finally:
        statement.release()



if __name__ == '__main__':

#let's create a test battery
    lock = threading.Lock()
    rlock = threading.RLock()
    condition = threading.Condition()
    mutex = threading.Semaphore(1)
    threading_synchronization_list = [lock ,rlock , condition , mutex]

#in the for cycle we call the threading_with e threading_no_with function
    for statement in threading_synchronization_list :
        t1 = threading.Thread(target=threading_with, args=(statement,))
        t2 = threading.Thread(target=threading_not_with, args=(statement,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()


    
    
