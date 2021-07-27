##Using Queue with multiprocessing – Section 3: Process Based Parallelism

import multiprocessing
import random
import time

"""
Existem duas formas de compartilhar objetos entre processos

1. Queue (filas): primeiro a ser adicionado pelo produtor é o primeiro a ser consumido pelo consumidor (FIFO)

2. Pipes
"""

"""
metodos de uma fila
- put: colocar (produtor) um procesos na fila
- get: pegar (consumidor) um processo na fila
"""

"""
Métodos adicionais de uma fila

- task_done() -> indica que uma tarefa está completa

- join() -> bloqueia o processo até que todas as tarefas da fila sejam performadas e processadas
"""
class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) :

        # adiciona 10 processos na fila a cada 1 segundo
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print ("Process Producer : item %d appended to queue %s"\
                   % (item,self.name))
            time.sleep(1)
            print ("The size of queue is %s"\
                   % self.queue.qsize())
        print('______________\nSTOP ADDING ITEMS ON QUEUE\n______________\n') # my modification

class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):                                                        
                # print("the queue is empty. Waiting items to consume")
                pass # my modification                                         
            else :
                # aguarda 2 segundos antes de pegar o item (objeto, pois no python tudo é objeto) da fila
                time.sleep(2)
                item = self.queue.get()
                print ('Process Consumer : item %d popped from by %s \n'\
                       % (item, self.name))
                time.sleep(1)


if __name__ == '__main__':
        queue = multiprocessing.Queue() # instanciando a fila
        process_producer = producer(queue) # passando a fila para o construtor do produtor
        process_consumer = consumer(queue) # passando a fila para o construtor do consumidor
        process_producer.start()
        process_consumer.start()
        process_producer.join()
        process_consumer.join()

"""
output:

Process Producer : item 120 appended to queue producer-1
the queue is empty
The size of queue is 1
Process Producer : item 255 appended to queue producer-1
The size of queue is 2
Process Producer : item 223 appended to queue producer-1
Process Consumer : item 120 popped from by consumer-2 
                  
The size of queue is 2
Process Producer : item 194 appended to queue producer-1
The size of queue is 3                                                                                       
Process Producer : item 110 appended to queue producer-1                                                     
Process Consumer : item 255 popped from by consumer-2 

The size of queue is 3
Process Producer : item 109 appended to queue producer-1
The size of queue is 4
Process Producer : item 158 appended to queue producer-1
The size of queue is 5
Process Producer : item 79 appended to queue producer-1
Process Consumer : item 223 popped from by consumer-2 

The size of queue is 5
Process Producer : item 89 appended to queue producer-1
The size of queue is 6
Process Producer : item 56 appended to queue producer-1
The size of queue is 7
Process Consumer : item 194 popped from by consumer-2 

Process Consumer : item 110 popped from by consumer-2 

Process Consumer : item 109 popped from by consumer-2 

Process Consumer : item 158 popped from by consumer-2 

Process Consumer : item 79 popped from by consumer-2 

Process Consumer : item 89 popped from by consumer-2 

Process Consumer : item 56 popped from by consumer-2 

the queue is empty
the queue is empty
the queue is empty
the queue is empty
...

"""