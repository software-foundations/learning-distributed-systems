import threading

mydata = threading.local()

print(mydata)

mydata.x = 1

print(mydata)

print(mydata.x)
