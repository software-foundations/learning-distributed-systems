#Using a process in a subclass – Section 3: Process Based Parallelism
import multiprocessing

class MyProcess(multiprocessing.Process):

	# sobrescrevendo o metodo run da classe Process
    def run(self):
        print ('called run method in %s' %self.name)
        return

if __name__ == '__main__':
    jobs = [] # lista de processos

    for i in range(5):
        p = MyProcess() # instancia o objeto Process (subclasse)
        jobs.append(p) # adiciona o processo na lista
        p.start() # inicaliza o processo
        p.join() # aguarda o proceso terminar para que execute a próxima instrução
