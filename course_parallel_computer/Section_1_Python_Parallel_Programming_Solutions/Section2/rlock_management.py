import threading
import time

class Box(object):
    lock = threading.RLock()
    # lock = threading.Lock() # my modification

    def __init__(self):
        self.total_items = 0

    def execute(self,n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()
        print('>>>>>>>>>> executed')
        print('total items: ', self.total_items, end='\n')

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()
        print("_______( + )________adder unlocked lock state: liberou\n\n")        

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()
        print("_______( - )________remover unlocked the lock state: liberou\n\n")



## These two functions run n in separate
## threads and call the Box's methods

def adder(box,items):
    while items > 0:
        print ("adding 1 item in the box: assumiu\n")
        box.add()
        time.sleep(2)
        items -= 1

def remover(box,items):
    while items > 0:
        print ("removing 1 item in the box: assumiu\n")
        box.remove()
        time.sleep(2)
        items -= 1


## the main program build some
## threads and make sure it works
if __name__ == "__main__":
    items = 5
    print ("putting %s items in the box \n\n\n" % items)
    box = Box()
    t1 = threading.Thread(target=adder,args=(box,items))
    t2 = threading.Thread(target=remover,args=(box,items))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print ("%s items still remain in the box " % box.total_items)

"""
ao usar lock = threading.RLock(), mais de uma thread pode assumir o controle do lock

É como se fosse um travamento encadeado
1. termina de executar
2. libera o travamento
3. vê quem assumiu o controle do travamento

Testar com e sem o tempo
Testar com o tempo só em uma thread
Testar com threading.Lock() e com threading.RLock()
"""

"""
output

putting 5 items in the box 



adding 1 item in the box: assumiu

>>>>>>>>>> executed
removing 1 item in the box: assumiu

total items:  1
_______( + )________adder unlocked lock state: liberou


>>>>>>>>>> executed
total items:  0
_______( - )________remover unlocked the lock state: liberou


removing 1 item in the box: assumiu

adding 1 item in the box: assumiu
>>>>>>>>>> executed

total items:  -1
_______( - )________remover unlocked the lock state: liberou


>>>>>>>>>> executed
total items:  0
_______( + )________adder unlocked lock state: liberou


removing 1 item in the box: assumiu

adding 1 item in the box: assumiu

>>>>>>>>>> executed
total items:  -1
_______( - )________remover unlocked the lock state: liberou


>>>>>>>>>> executed
total items:  0
_______( + )________adder unlocked lock state: liberou


removing 1 item in the box: assumiu

adding 1 item in the box: assumiu

>>>>>>>>>> executed
total items:  -1
_______( - )________remover unlocked the lock state: liberou


>>>>>>>>>> executed
total items:  0
_______( + )________adder unlocked lock state: liberou


removing 1 item in the box: assumiu

>>>>>>>>>> executed
total items:  -1
_______( - )________remover unlocked the lock state: liberou


adding 1 item in the box: assumiu

>>>>>>>>>> executed
total items:  0
_______( + )________adder unlocked lock state: liberou


0 items still remain in the box 
"""

