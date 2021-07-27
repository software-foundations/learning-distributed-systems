print ("called_Process_2.py!!")
closeInput = input("Press ENTER to exit")

# my modification
"""
this module calls calling_Process.py one, wich calls this module again
"""
import os
import sys

program = "/home/bruno/Documents/dev/learning-distributed-systems/venv-learning-distributed-systems/bin/python" # path for my virtual python interprerter
# program = "/home/bruno/Documents/dev/sist_dist_p1/python/venv-sist-dist-p1/bin/python"

arguments = ["calling_Process.py"]
# os.execvp(program, (program,)+ tuple(arguments))
os.execvp(program, (program, arguments[0]))