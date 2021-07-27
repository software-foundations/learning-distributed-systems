import Pyro4

"""
terminal 03: python client.py
	type: server
"""
uri = input("insert the PYRO4 server URI (help : PYRONAME:server) ").strip()
print(f"uri: {uri, type(uri)}")

name = input("What is your name? ").strip()
# use name server object lookup uri shortcut
server = Pyro4.Proxy("PYRONAME:server")    
print(server.welcomeMessage(name))
