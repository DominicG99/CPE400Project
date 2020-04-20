# Authors: Dominic Ginter, <Insert Name 2>, <Insert Name 3>
# CPE 400 Project
# Hierarchial Routing Simulation
import matplotlib as plt
import math
import networkx as nx # This is for creating graphs
network = nx.MultiGraph()
network.add_nodes_from([0,36])
network.add_edges_from([(0,1),(0,3),(1,2),(2,3)], weight = 1.0) #Cluster 1 Region 1 Connections
network.add_edges_from([(4,5),(4,7), (5,6), (6,7)], weight = 1.0) #Cluster 1 Region 2 Connections
print("This program simulates Multilevel hierarchial routing with an example network.\nThis example network can be found inside the project folder.\n") #Brief Description
while True: # This will keep the program running until the user decides to quit.
    print("Please select an option.\n1.Route Packets in Network\n2.Display Routing Table\n3.List Border Gateway Routers\n4.Exit Program") #Menu print
    cmd = input() #collect user input
    if cmd == '1':
        print("Enter a source address: ")
        srcAdd = input() # User will enter source router address from example network
        print("Enter a destination address: ")
        dstAdd = input() # User will enter destination router address from example network
        break
    elif cmd == '2':
        print("Enter a router address: ") # User will enter a router address from example network
        rtrAdd = input()
        print("Would you like to see the full table or hierarchial table? (Please type 1 for full table or 2 for hierarchial table.") #This will show the difference between full table and hierarchial table
        tableChoice = input()
        if tableChoice == '1':
            print("In the works.")
            # Will print the full routing table here
        elif tableChoice == '2':
            print("In the works.")
            # Will print the hierarchial routing table here
        break
    elif cmd == '3':
        print("I'm thinking we make a function to list the level 1 and 2 BG routers")
        break
    elif cmd == '4':
        break
