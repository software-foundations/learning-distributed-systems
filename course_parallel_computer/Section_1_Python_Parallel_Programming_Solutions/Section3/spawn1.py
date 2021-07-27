import multiprocessing
import target_function

"""
Paralelismo de um objeto processo em três etapas:

1. criar o objeto processo

2. obj_process.start() -> inicia o processo

3 obj_process.join() -> espera até que o processo termine para ir para a próxima instrução da thread que chamou o processo

Agora, a função é criada em outro modulo e importada para cá,
mas funciona da mesma forma que o módulo spawn_a_process.py

"spawn a process" significa "gerar um processo"
"""
if __name__ == '__main__':
 Process_jobs = []
 for i in range(5):
     p = multiprocessing.Process \
     (target=target_function.function,args=(i,))
     Process_jobs.append(p)
     p.start()
     p.join()
