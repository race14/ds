#!/usr/bin/env python
# coding: utf-8

# In[ ]:


############MyClient.java##################
import java.rmi.Naming;
import java.util.Scanner;

public class MyClient {
    public static void main(String[] args) {
        try {
            MyInterface obj = (MyInterface) Naming.lookup("//localhost/MyRemoteClass");
            Scanner sc = new Scanner(System.in);
            
            System.out.print("Enter first number: ");
            int a = sc.nextInt();
            
            System.out.print("Enter second number: ");
            int b = sc.nextInt();
            
            System.out.println("The addition is: " + obj.addition(a, b));
            System.out.println("The multiplication is: " + obj.mult(a, b));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

###############// MyServer.java########################
import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class MyServer {
    public static void main(String[] args) {
        try {
            MyInterface obj = new MyRemoteClass();
            LocateRegistry.createRegistry(1099);
            Naming.rebind("//localhost/MyRemoteClass", obj);
            System.out.println("MyRemoteClass bound in registry");
        } catch (Exception e) {
            System.err.println("MyRemoteClass exception:");
            e.printStackTrace();
        }
    }
}


############MyRemoteClass.java##################
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class MyRemoteClass extends UnicastRemoteObject implements MyInterface {
    public MyRemoteClass() throws RemoteException {
        super();
    }

    @Override
    public int addition(int x, int y) throws RemoteException {
        return x + y;
    }

    @Override
    public int mult(int x, int y) throws RemoteException {
        return x * y;
    }
}


##################// MyInterface.java#####################
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface MyInterface extends Remote {
    int addition(int x, int y) throws RemoteException;
    int mult(int x, int y) throws RemoteException;
}




