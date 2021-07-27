##Using Pipes with multiprocessing – Section 3: Process Based Parallelism

import multiprocessing

"""
Pipe() explanation

multiprocessing.Pipe([duplex])
Returns a pair (conn1, conn2) of Connection objects representing the ends of a pipe.

If duplex is True (the default) then the pipe is bidirectional. If duplex is False then the pipe is unidirectional: conn1 can only be used for receiving messages and conn2 can only be used for sending messages.

Methods:
send -> send an object to the other side of the pipe (for the other connection)
recv -> receiv an object to the other side of the pipe
"""

"""
output_conn, input_conn = pipe_1 ou pipe_2

pipe_1 envia
pipe_2 recebe

    # o output é o processo para o qual será enviado os objetos

    # o input é o processo que vai receber


"""
def create_items(pipe):
    output_pipe, _ = pipe
    # envia 10 items para a outra ponta da conexão
    for item in range(10):
        print('send an item') # my modification
        output_pipe.send(item) # envia todos os items, um por umm para o pipe que armazena na ordem em que foram enviados e, depois, o processo para o qual foi enviado consome com recv na mesma ordem de envio. Acaba funcionando como uma fila        
    output_pipe.close()

def multiply_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close() # fecha a conexão do objeto que recebe, para que este objeto possa enviar
    output_pipe, _ = pipe_2
    try:
        while True:
            item = input_pipe.recv()
            output_pipe.send(item * item)
    except EOFError:
        # https://www.geeksforgeeks.org/handling-eoferror-exception-in-python/
        # https://docs.python.org/3/library/exceptions.html
        print('item is empty') # my modification
        output_pipe.close()


if __name__== '__main__':

#First process pipe with numbers from 0 to 9
    pipe_1 = multiprocessing.Pipe(True) # Cria o pipe 01
    # cria o processo do pipe 01, que vai
    process_pipe_1 = \
                   multiprocessing.Process\
                   (target=create_items, args=(pipe_1,))
    process_pipe_1.start()
    # process_pipe_1.join() # my modification -> nao faz diferenca

#second pipe,
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = \
                   multiprocessing.Process\
                   (target=multiply_items, args=(pipe_1, pipe_2,))
    process_pipe_2.start()

    # my modification
    print('\npipe 01 connections')
    [print(conn) for conn in pipe_1]
    print('\npipe 02 connections')
    [print(conn) for conn in pipe_2]

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:

            print (pipe_2[1].recv())
    except EOFError:
        print ("End")
