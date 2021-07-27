import threading

shared_resource_with_lock     = 0
shared_resource_with_no_lock     = 0
COUNT = 100000
shared_resource_lock = threading.Lock()


####LOCK MANAGEMENT##
def increment_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock += 1
        shared_resource_lock.release()

def decrement_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -= 1
        shared_resource_lock.release()
        
####NO LOCK MANAGEMENT ##
def increment_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock += 1
 
def decrement_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock -= 1
 
####the Main program
if __name__ == "__main__":
    t1 = threading.Thread(target = increment_with_lock)
    t2 = threading.Thread(target = decrement_with_lock)
    t3 = threading.Thread(target = increment_without_lock)
    t4 = threading.Thread(target = decrement_without_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print ("the value of shared variable with lock management is %s"\
           %shared_resource_with_lock)
    print ("the value of shared variable with race condition is %s"\
           %shared_resource_with_no_lock)

"""
Com lock, threads concorrentes não acessam uma variável na memória compartilhada ao mesmo tempo, aguardando até que uma operação seja finalizada para inicializar a outra operação que também acessa a mesma variável na memória compartilhada.

Sem lock, threads concorrentes podem acessar uma variável na memória ao mesmo tempo, podendo haver atribuição incorreta de valores dado o acesso simultâneo a uma variável na memória compartilhada.

Agora uma dúvida: como as variáveis foram declaradas no escopo da thread principal, eles são variáveis da thread principal do processo, que é armazenada na memória do processo, logo, é compartilhada por todas as subthreads dentro da thread principal do processo.

Portanto, o estado de uma thread (ao tentar acessar uma variável na memória comartilhada do processo principal para a thread principal e para as subthreads) pode ser: locked ou unlocked

- Se o estado for unlocked, uma chamada para aquire() muda o estado para locked

- Se o estado for locked, uma chamada para aquire() é bloqueia a thread até que uma outra thread chame release()

- Se o estado for unlocked, uma chamada para release() levanta Runtime Error Error exception

- Se o estado for locked, uma chamda para release() muda o estado da thread para destravado

----

Desvantagens:
1. Locks são subjetivos e podem causar deadlocks
2. Locks possuem vários outros pontos negativos para a aplicação como um todo
3. Locks limita a escalabilidade  e compromete a legibilidade do código
4. O uso the lock (travamento) em conflito com a possível necessidade de impor prioridade de acesso a memory compartilhada por vários processos
5. Uma aplicação que contém um lock (travamento) apresenta considerável dificuldade de identificar pontos exatos de erro
"""
