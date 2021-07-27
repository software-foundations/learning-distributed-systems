import threading
import time

"""
Associo Threads a funções
Nomeio Threads
Pego o nome de threads nomeadas
"""

# my modification: thread id's

def first_function():    
    print ('thread id: ', threading.get_ident(), threading.currentThread().getName() + str(' is Starting \n'))
    time.sleep(2)
    print ('thread id: ', threading.get_ident(), threading.currentThread().getName() + str(' is Exiting \n'))
    return

def second_function():    
    print ('thread id: ', threading.get_ident(), threading.currentThread().getName() + str(' is Starting \n'))
    time.sleep(2)    
    print ('thread id: ', threading.get_ident(), threading.currentThread().getName() + str(' is Exiting \n'))
    return

def third_function():    
    print ('thread id: ', threading.get_ident(), threading.currentThread().getName() + str(' is Starting \n'))
    time.sleep(2)    
    print ('thread id: ', threading.get_ident(), threading.currentThread().getName() + str(' is Exiting \n'))
    return


if __name__ == "__main__":
    t1 = threading.Thread(name='first_function', target=first_function)
    t2 = threading.Thread(name='second_function', target=second_function)
    t3 = threading.Thread(name='third_function', target=third_function)



    t1.start()
    t2.start()
    t3.start()
    
    # join([timeout]) Wait until the thread terminates
    # https://stackoverflow.com/questions/15085348/what-is-the-use-of-join-in-python-threading

    t1.join()
    print(t1.is_alive())
    print('t1 joined')# my modifications -> this line is executed when t1 terminates
    # print('press to continue and execute t2: ', input()) # but in fact, the t2 had already been started and proplably had already been executed. The same happens with the other threads
    t2.join()
    print(t2.is_alive())
    print('t2 joined')# my modifications -> this line is executed when t2
    # print('press to continue: ', input())
    # print('press to continue and execute t3: ', input())    
    t3.join()
    print(t3.is_alive())
    print('t3 joined')# my modifications -> this line is executed when t2
    # print('press to finish the main thread: ', input())

"""
output:
thread id:  140204642060032 first_function is Starting 

thread id:  140204633667328 second_function is Starting 

thread id:  140204625274624 third_function is Starting 

thread id:  140204642060032 first_function is Exiting 
thread id:  140204625274624 third_function is Exiting 

thread id:  140204633667328 second_function is Exiting 
"""

