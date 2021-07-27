import time
from threading import Thread, Event
import random

items = []
event = Event()
"""
Summary
event.wait() -> used by consumer to wait an event occurs to continue its processing
event.set() -> set the Event, notifying the consumer
event.clear() -> Event is set to false by clear() method"
"""

class consumer(Thread):
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event
    
    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            print ('Consumer notify : %d popped from list by %s' %(item, self.name))
            print('###\nitems: {}'.format(items))
            

class producer(Thread):
    def __init__(self, integers, event):
        Thread.__init__(self)
        self.items = items
        self.event = event
    
    def run(self):
        global item
        for i in range(100):
            time.sleep(2)
            item = random.randint(0, 256)
            self.items.append(item) 
            print ('Producer notify : item %d appended to list by %s' % (item, self.name))
            print ('Producer notify : event set by %s' % self.name)
            self.event.set()

            # print ('Produce notify : event cleared by %s \n' % self.name)
            self.event.clear() # se não for executado o método clear, o consumidor pode não ser notificado devido a falha de sincronização

            # ai da o seguinte erro:
            """
            Exception in thread Thread-2:
            Traceback (most recent call last):
              File "/usr/lib/python3.8/threading.py", line 932, in _boot
            """
            # após o erro da Thread do consumidor, a thread do produtor fica adicionando items mesmo que a thread do consumidor não os consuma


if __name__ == '__main__':
    t1 = producer(items, event)
    t2 = consumer(items, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
 
