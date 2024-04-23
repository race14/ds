#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import java.util.Scanner;

class five{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the number of nodes:");
        int n = scan.nextInt();
        int token = 0, ch;

        do {
            System.out.println("Enter sender:");
            int sender = scan.nextInt();
            System.out.println("Enter receiver:");
            int receiver = scan.nextInt();
            System.out.println("Enter data:");
            int data = scan.nextInt();

            System.out.print("Token passing: ");
            for (int i = token; i % n != sender; i++) {
                System.out.print((i % n) + " -> ");
            }
            System.out.println(sender);
            System.out.println("Sender " + sender + " sending data: " + data);
            for (int i = (sender + 1) % n; i != receiver; i = (i + 1) % n) {
                System.out.println("Data " + data + " forwarded by " + i);
            }
            System.out.println("Receiver " + receiver + " received data: " + data + "\n");

            token = sender;
            System.out.println("Do you want to send again? Enter 1 for Yes and 0 for No:");
            ch = scan.nextInt();
        } while (ch == 1);

        scan.close();
    }
}

