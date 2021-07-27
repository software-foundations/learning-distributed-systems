

import multiprocessing
import time

"""
importante

possiveis valores de código de saída

1. ==0 : não houve erros

2. >0: houve erro

3. <0: não ouve erro, mas o processo foi matado, onde o valor significa -1 * ExitCode
"""

def foo():
    print ('Starting function')
    time.sleep(0.1)
    print ('Finished function')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print ('Process before execution:', p, p.is_alive())

    p.start()
    print ('Process running:', p, p.is_alive())

    p.terminate()

    # time.sleep(5) # my modification
    """
    Quando coloco esse termporizado de 5 segundos, a saída fica assim

    Process before execution: <Process name='Process-1' parent=11720 initial> False
    Process running: <Process name='Process-1' pid=11721 parent=11720 started> True
    Process terminated: <Process name='Process-1' pid=11721 parent=11720 stopped exitcode=-SIGTERM> False
    Process joined: <Process name='Process-1' pid=11721 parent=11720 stopped exitcode=-SIGTERM> False
    Process exit code: -15

    #######
    ou seja, é como se o processo terminasse depois da execução da próxima instrução, o que não deveria acontecer
    """

    print ('Process terminated:', p, p.is_alive())

    p.join()
    print ('Process joined:', p, p.is_alive())

    print ('Process exit code:', p.exitcode)

"""
Process before execution: <Process name='Process-1' parent=11490 initial> False                              
Process running: <Process name='Process-1' pid=11491 parent=11490 started> True
Process terminated: <Process name='Process-1' pid=11491 parent=11490 started> True                           
Process joined: <Process name='Process-1' pid=11491 parent=11490 stopped exitcode=-SIGTERM> False            
Process exit code: -15
"""
