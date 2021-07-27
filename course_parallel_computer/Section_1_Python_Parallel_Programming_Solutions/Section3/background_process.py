import multiprocessing
import time

"""
Como já vimos anteriormente,
o demaon é uma variável boooleana
- deamon=True -> processo rodará em background
- demaon=Fals (DEFAULt) -> processo não rodará em background

Processo que roda em background não terá interação com o usuário

Isso pode ser útil em questões de segurança, restringindo a intervenção
do usuário em processos que são críticos para a integridade do sistema
e integridade de dados do sistema

importante

- processos que não estão no modo de background possuem output no terminal, então os processos em background morrem automaticamente quando o processo que os chamou morre

- processo que estão no background não possuem output no terminal

- processos em background não podem criar processo filhos
"""
def foo():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" %name)
    time.sleep(3)
    print ("Exiting %s \n" %name)
    

if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='background_process',\
                          target=foo)
    background_process.daemon = True
    """
    O processo em background não vai printar nada no terminal, mesmo que
    a função que executa no processo possua prints.

    Isso é feito automaticamente pelo interpretador
    """

    NO_background_process = multiprocessing.Process\
                            (name='NO_background_process',\
                             target=foo)
    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
    

