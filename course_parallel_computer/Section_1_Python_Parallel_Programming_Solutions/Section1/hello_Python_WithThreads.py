## To use threads you need import Thread using the following code:
from threading import Thread, get_ident # my modification: get_ident
import os # my modification

##Also we use the sleep function to make the thread "sleep" 
from time import sleep

## To create a thread in Python you'll want to make your class work as a thread.
## For this, you should subclass your class from the Thread class
class CookBook(Thread):
    """
    This class is a Thread
    Each instance of this class is a difference Thread object
    """
    # def __init__(self): # my modification
    def __init__(self, i):

        Thread.__init__(self)
        self.message = "Hello Parallel Python CookBook!!\n"
        self.i = i

##this method thod prints only the message 
    def print_message(self):
        print (self.message)

##The run method prints ten times the message 
    def run(self):
        # print (f"Thread {get_ident()} Starting\n")

        # My modification
        # https://www.kite.com/python/answers/how-to-get-the-id-of-a-thread-in-python        
        # print('process id: ', os.getpid())

        x=0
        print (f">>>Thread {get_ident()} Started\n")        
        while (x < 10):
            # print('process id: ', os.getpid())

            # self.print_message() # my modification
            # print('\ni: ', self.i, end='\t')
            # print(f'thread id of loop {x}: ', get_ident()) # my modification
            # print('x: ', x)
            # print(f'i: {i}, thread: {get_ident()}, x: {x}')
            print(f'thread: {get_ident()}, x: {x}')

            # sleep(2)
            x += 1
        print (f">>>Thread {get_ident()} Ended\n")

        # My modification
        # https://www.kite.com/python/answers/how-to-get-the-id-of-a-thread-in-python
        # print('main thread: ', get_ident())


#start the main process
# print ("Process Started")

# create an instance of the HelloWorld class
# hello_Python = CookBook(10)

# print the message...starting the thread
# hello_Python.start()

#end the main process
# print ("Process Ended")

# my modification
print('\n\n__________MULTIPLE THREADS AT THE SAME PROCESS WITHOUT MODIFY THE Global Locker Interpreter (multiplex threads, executing one per time)_________\n\n')
print('process id: ', os.getpid())

li_thread_obj = []

for i in range(2):
    # print('\n\n___INITIALIZING THREAD___\n\ni: ', i)
    li_thread_obj.append(CookBook(i))

ts = map(lambda t: t.start(), li_thread_obj)
[t for t in ts]

"""
Dá pra ver que i = 0 não é atribuído corretamente para cada thread object, porém, cada thread object executa a em thread separado, ambos dentro do mesmo processo
"""