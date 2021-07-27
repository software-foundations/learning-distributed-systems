#Spawn a Process – Section 3: Process Based Parallelism
import multiprocessing

"""
Paralelismo de um objeto processo em três etapas:

1. criar o objeto processo

2. obj_process.start() -> inicia o processo

3 obj_process.join() -> espera até que o processo termine para ir para a próxima instrução da thread que chamou o processo
"""
def function(i):
    print ('called function in process: %s' %i)
    return

if __name__ == '__main__':
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=function, args=(i,))
        Process_jobs.append(p)
        p.start()
        p.join()
