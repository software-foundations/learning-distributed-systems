#hello.py
"""
Para instalar a dependência mpi.h de mp4py, seguir um dos dois tutoriais

https://stackoverflow.com/questions/26920083/fatal-error-mpi-h-no-such-file-or-directory-include-mpi-h

https://gist.github.com/pajayrao/166bbeaf029012701f790b6943b31bb2

"""
"""
O que funcionou para mim, porém acho ruim porque instala pacotes desnecessários de fortran

sudo apt install libopenmpi-dev
"""
"""
instalar agora mpi4py
pip install mpi4py
"""
from multiprocessing import cpu_count

from mpi4py import MPI
comm = MPI.COMM_WORLD	# objeto para fazer a comunicação
# print('type(comm): ', type(comm))
rank = comm.Get_rank()	# pega o processo/processador
# print('type(rank): ', type(rank), 'rank: ' ,rank)

# try change of place these two lines above
print ("hello world from process ", rank) # when this line is executed, the lines above is ignored
print('sasasas{}'.format(cpu_count())) # the lines above of with cpu_count() where executed at other time
print('n. cores: ', cpu_count()) # n of total threads supported
print()
"""
para executar
helloworldwithMPI.py
ou
mpiexec -n 2 python helloworldwithMPI.py

-n especifica o número de núcleos
no caso do meu notebook, ele só possui 2 núcleos, cada um com 4 threads

Então quando eu executo os.cpu_count() e retorna 4 deve ser o número de threads por núcleo. O mesmo ocorre com multiprocessing.cpu_count()
"""

