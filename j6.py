#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import java.util.*;

class Node{
    int id;
    boolean isCoordinator;

    public Node(int nodeId) {
        this.id = nodeId;
        this.isCoordinator = false;
    }

    public void initiateElection(List<Node> nodes) {
        for (Node node : nodes) {
            if (node.id > this.id) {
                System.out.printf("Node %d sends election message to Node %d%n", this.id, node.id);
                node.initiateElection(nodes);
            }
        }
        this.isCoordinator = true;
        System.out.printf("Node %d becomes the coordinator.%n", this.id);
    }

    public static void main(String[] args) {
        List<Node> nodes = new ArrayList<>();
        for (int i = 1; i <= 5; i++) {
            nodes.add(new Node(i));
        }

        System.out.println("Bully Algorithm:");
        nodes.get(4).initiateElection(nodes); // Highest ID starts the election

        System.out.println("\nRing Algorithm:");
        nodes.get(0).initiateElection(nodes); // Lowest ID starts the election
    }
}

