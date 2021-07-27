import threading
import time

# ainda não entendo o uso dessa exit flag
exit_Flag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print ("Starting " + self.name + "\n")
        print_time(self.name, self.counter, 5)
        print ("Exiting " + self.name + "\n")

def print_time(threadName, delay, counter):
    while counter:
        if exit_Flag:
            thread.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

#Main program
if __name__ == '__main__':
    # Create two threads
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    # Start the Threads created
    thread1.start()
    thread2.start()

    # Wait for all thread to complete 
    thread1.join()
    print('----------')
    thread2.join()
    print('t1 and t2 subthreads have been both finished and exited sucessfuly')    
    
    print ("Exiting Main Thread")

    """
    As threads thread1 e thread2 vão ser executadas em paralelo, porém, são disparadas em ordem ao implementar thread1.start() e thread2.start() nesta ordem.

    O delay da thread1 é de 1 segundo, logo, print_time levará 5 segundo para printar 5 vezes.

    O delay da thread2 é de 2 segundos, logo, print_time levará 10 segundo para printar 5 vezes.

    thread1.join() para a execução da thread principal, aguardando até que a thread1 seja finalizada.

    Quando a thread 1 é finalizada, é printado na tela '----------'

    thread2.join() para a execução da thread principal, aguardando até que a thread2 seja finalizada.

    É printado na tela 't1 and t2 subthreads have been both finished and exited sucessfuly'

    É printado na tela 'Exiting the main thread'
    """    



