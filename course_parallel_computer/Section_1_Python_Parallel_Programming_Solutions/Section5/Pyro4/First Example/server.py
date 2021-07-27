import Pyro4


"""
in terminal 01:
python -m Pyro4.naming

in terminal 02:
python server.py
"""

@Pyro4.expose # wihtout this line the client doesn't run properly
class Server(object):
    def welcomeMessage(self, name):
        return ("Hi welcome " + str (name))

def startServer():
    server = Server()

    # make a Pyro daemon to listen remote calls
    # all pyro objects are registered in one or more deamons
    daemon = Pyro4.Daemon() 

    # locate the name server running
    # usually there is just one name server running in your network
    ns = Pyro4.locateNS()

    # register the server as a Pyro object
    # uri is unique resource identifier (the same idea of url - unique resource location)
    uri = daemon.register(server)  
    
    # register the object with a name in the name server
    ns.register("server", uri)   
    
    # print the uri so we can use it in the client later
    print("Ready. Object uri =", uri)
    
    # start the event loop of the server to wait for calls
    daemon.requestLoop()                   

if __name__ == "__main__":
    startServer()

