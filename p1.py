
###server.py

# pip install pyro4

# pyro4-ns  ---> tarminal command to run sever 

import Pyro4

@Pyro4.expose
class MyRemoteClass(object):
    def addition(self, x, y):
        return x + y

    def mult(self, x, y):
        return x * y

def main():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(MyRemoteClass)
    ns.register("MyRemoteClass", uri)
    print("Server is ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
    
    
    
    
#########client.py########

import Pyro4

def main():
    try:
        uri = "PYRONAME:MyRemoteClass"
        obj = Pyro4.Proxy(uri)
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("The Addition is:", obj.addition(a, b))
        print("The Multiplication is:", obj.mult(a, b))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

