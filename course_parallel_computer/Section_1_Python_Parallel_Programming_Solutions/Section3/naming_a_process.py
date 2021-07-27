#Naming a Process – Section 3: Process Based Parallelism
import multiprocessing
import time

def foo():
    print(multiprocessing.current_process().name)
    name = multiprocessing.current_process().name # takes the name ("Process-integer" by DEFAULT) that identifies the process
    print ("Starting %s \n" %name)
    time.sleep(3)
    print ("Exiting %s \n" %name)

if __name__ == '__main__':
  """
  Agora não enteb
  """
  process_with_name = \
                    multiprocessing.Process\
                    (name='foo_process',\
                     target=foo)
  process_with_name.daemon = True # demaon=True indicate that the process will run in background, without user interaction
  process_with_default_name = \
                            multiprocessing.Process\
                            (target=foo)
  process_with_name.start()
  print("process with name: ", process_with_name.__str__()) # aqui printa "foo-process" -> Nome setado manualmente

  process_with_default_name.start()
  print("process with default name name: ", process_with_default_name.__str__()) # aqui printa "Process-integer", -> DEFAULT
