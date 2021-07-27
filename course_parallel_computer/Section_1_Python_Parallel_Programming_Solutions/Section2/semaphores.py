###Using a Semaphore to synchronize threads

import threading
import time
import random

##The optional argument gives the initial value for the internal counter;
##it defaults to 1.
##If the value given is less than 0, ValueError is raised.
semaphore = threading.Semaphore(0)

def consumer():
    print ("consumer is waiting.")
    ##Acquire a semaphore
    semaphore.acquire()
    ##The consumer have access to the shared resource
    print ("Consumer notify : consumed item number %s " %item)


def producer():
    global item
    time.sleep(10)
    ##create a random item
    item = random.randint(0,1000)
    print ("producer notify : producted item number %s" %item)
    
    ##Release a semaphore, incrementing the internal counter by one.
    ##When it was zero on entry and another thread is waiting for it
    ##to become larger than zero again, wake up that thread.
    semaphore.release()


#Main program
if __name__ == '__main__':
    for i in range (0,5) :
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print ("program terminated")

"""
A variável semafore limita a quantidade de threads acessando uma variável ou um recurso

A variável semafore é um inteiro que determina o número de threads que ainda podem acessar o recurso.


A operação semafore.aquire() indica que uma thread está acessando a um recurso e decrementa o semafore.

A operação semafore.release() indica que uma thread está liberando o acesso a um recurso e incrementa o semafore

Cada operação de uma thread da aplicação consumer para acessar um recurso controlado por semáfaro deve ser precedida pela operação semafore.aquire()

Cada operação de uma thread da aplicação producer para acessar um recurso controlado por semáforo

In general, a resource can only be acessed if the semafore value is greather than 0

Logo, como semafore é 0, somente quando o produtor(thread) libera o recurso o consumidor(outra thread) consegue acessá-lo

- thread producer start (starts first then consumer does)
- thread consumer start

1. semafore = 0
2. consumer waiting for the resource resource:
3. producer (release) -> semafore 0 -> semafore 1
4. consumer consums the resource ()

# Vantagens

Um uso particular dos semaforos é a o mutex (abreviação de mutually exclusive) o qual é nada mais nada menos que um semaforo com um valor de inicialização do semáforo é 1

Isso permite a realização de exclusão mútua em acesso a dados e recursos

Semáforos ainda são comummente utilizados em linguagens de programação que são multithreads
"""