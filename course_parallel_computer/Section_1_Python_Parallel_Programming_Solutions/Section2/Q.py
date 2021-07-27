from threading import Thread, Event
from queue import Queue
import time
import random
import sys

"""
Trabalhar com filas facilita o uso de Threads de forma clara e concisa
evitando acesso simultâneo a items por parte dos clientes
>> QUEUE Methods

put() -> puts an item on a queue

get() -> get and remove an item  on a queue

task_done() -> need to be called each time an item has been processed

join() -> block until all items have been processed

>> Two possibilities:

1 - If optional args block is true and timeout is None -> Block until a free slot is available (default case use in the example of the class)

2 - If the blocks is false - Put an item in the queue if a free slot is immediately available or raise the full exception
"""
class producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(100):
            item = random.randint(0, 256)
            self.queue.put(item)
            print ('Producer notify : item N° %d appended to queue by %s \n'\
                   % (item, self.name))
            print('______________________QUEUE: ', list(queue.queue))
            """
            As vezes print a lista vazia porque entre a adição do item na fila e o print da fila uma thread já consumiu o item recem adicionado
            """
            time.sleep(0.1)        

class consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print ('Consumer notify : %d popped from queue by %s'\
                   % (item, self.name))

            """
            Esse for é para adicionar tempo de "processamento" no processamento do item
            """
            # print(int(item))
            a = []
            for i in range(random.choice([0,1000000]) * int(item)):
                a.append(i)


            self.queue.task_done()


if __name__ == '__main__':
        queue = Queue()
        t1 = producer(queue)
        t2 = consumer(queue)
        t3 = consumer(queue)
        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()

        # e se eu tirar os join() ?
        """
        O processo trava na thread que não tem join()
        Logo, se duas threads deveriam ser executadas em paralelo, então as threads não precisam ficar esperando o fim uma da outra
        """

