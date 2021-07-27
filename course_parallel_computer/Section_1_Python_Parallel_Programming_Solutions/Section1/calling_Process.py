##The following modules must be imported
import os
import sys
##this is the code to execute

# my modification
# program = "python"

# my modification

program = "/home/bruno/Documents/dev/learning-distributed-systems/venv-learning-distributed-systems/bin/python" # path for my virtual python interprerter

print("Process calling")
arguments = ["called_Process.py"]
# arguments = ["called_Process.py", "called_Process_2.py"] # my modification: doesn't work

# my modification starts
print('1, ', (program,)+ tuple(arguments)) # sum tuple with tuple
print('2, ', (program,), type((program,))) # the "," turn it into a tuple
print('3, ', (program), type((program))) # my modification
print('4, ', tuple(arguments)) # 
# my modification ends


##we call the called_Process.py script
# https://www.kite.com/python/docs/os.execvp
os.execvp(program, [program, "called_Process_2.py"])
# os.execvp(program, (program,)+ tuple(arguments))

# my modification
print('Finished the calling process') # this message will never be displayed



