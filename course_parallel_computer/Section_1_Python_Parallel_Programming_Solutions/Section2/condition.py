from threading import Thread, Condition
import time

items = []
condition = Condition()

class consumer(Thread):
	def __init__(self):
		Thread.__init__(self)

	def consume(self):
		global condition
		global items	

		# print('condition.wait (consumer -  before condition.aquire()): {}'.format(condition.wait()))		
		"""
		Raises an error:

		raise RuntimeError("cannot wait on un-acquired lock")
		RuntimeError: cannot wait on un-acquired lock
		Exception in thread Thread-2

		"""
		condition.acquire()
		# print('condition.wait (consumer - after condition.aquire()): {}'.format(condition.wait()))
		"""
		Como a thread consumer adquiriu a condição para execução e depois diz que fica esperando pela liberação da condição, ela se trava.

		Enquanto isso, o produtor continua produzindo, mas o consumidor não consome.

		O estranho é que items.pop() não é executado, mas estas linhas abaixo são

		print("Consumer notify : consumed 1 item")
		print("Consumer notify : items to consume are "\
                      + str(len(items)))

		"""

		if len(items) == 0:

			condition.wait()
			"""
			Se não houver items a serem consumidos, o consumidor aguarda o produtor ...

			1. gerar items
			2. condition.notify()
			3. condition.release()

			"""
			print("Consumer notify : no item to consume")
		items.pop()
		print("Consumer notify : consumed 1 item")
		print("Consumer notify : items to consume are "\
                      + str(len(items)))
		condition.notify() # notifica a próxima thread da fila que o recurso vai ser liberado, sinalizado pelo release da condição
		# condition.notify_all() notifica todas as threads da fila
		condition.release()
		
	def run(self):
		for i in range(0,20):
			time.sleep(10)
			self.consume()
			

class producer(Thread):
	def __init__(self):
		Thread.__init__(self)

	def produce(self):
		global condition
		global items

		# print('condition.wait (producer) - before condition.aquire(): {}'.format(condition.wait()))

		"""
		Exception in thread Thread-1:

		raise RuntimeError("cannot wait on un-acquired lock")
		RuntimeError: cannot wait on un-acquired lock
		"""
		condition.acquire()
		# print('condition.wait (producer) - after condition.aquire(): {}'.format(condition.wait()))
		"""
		Fica esperando pela notificação de término da thread em execução
		Como a thread em execução é essa mesma que fica esperando, então esta thread para e fica esperando o término da execução dela mesma. Logo, o programa para, pois o produtor fica esperando por ele mesmo e o consumidor, que fica esperando pelo produtor, também está parado.
		"""

		if len(items) == 10:
			condition.wait()
			"""
			Se o número de items a serem consumidos for igual a 10 (tome 10 como o tamanho máximo do buffer de items a serem consumidos), o produtor aguarda o produtor ...

			1. consumir items
			2. condition.notify()
			3. condition.release()
			
			"""
								
			print("Producer notify : items producted are "\
                              + str(len(items)))
			print("Producer notify : stop the production!!")
		items.append(1)
		print("Producer notify : total items producted "\
                      + str(len(items)))
		condition.notify()
		condition.release()

	def run(self):
		for i in range(0,20):
			time.sleep(5)
			self.produce()			

if __name__ == "__main__":
        producer = producer()
        consumer = consumer()
        producer.start()
        consumer.start()
        producer.join()
        consumer.join()

"""
https://docs.python.org/3/library/threading.html

Condition Objects
A condition variable is always associated with some kind of lock; this can be passed in or one will be created by default. Passing one in is useful when several condition variables must share the same lock. The lock is part of the condition object: you don’t have to track it separately.

A condition variable obeys the context management protocol: using the with statement acquires the associated lock for the duration of the enclosed block. The acquire() and release() methods also call the corresponding methods of the associated lock.

Other methods must be called with the associated lock held. The wait() method releases the lock, and then blocks until another thread awakens it by calling notify() or notify_all(). Once awakened, wait() re-acquires the lock and returns. It is also possible to specify a timeout.

The notify() method wakes up one of the threads waiting for the condition variable, if any are waiting. The notify_all() method wakes up all threads waiting for the condition variable.

Note: the notify() and notify_all() methods don’t release the lock; this means that the thread or threads awakened will not return from their wait() call immediately, but only when the thread that called notify() or notify_all() finally relinquishes ownership of the lock.

The typical programming style using condition variables uses the lock to synchronize access to some shared state; threads that are interested in a particular change of state call wait() repeatedly until they see the desired state, while threads that modify the state call notify() or notify_all() when they change the state in such a way that it could possibly be a desired state for one of the waiters. For example, the following code is a generic producer-consumer situation with unlimited buffer capacity:
"""