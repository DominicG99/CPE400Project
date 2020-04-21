# Authors: Dominic Ginter, <Insert Name 2>, <Insert Name 3>
# CPE 400 Project
# Hierarchial Routing Simulation
import matplotlib.pyplot as plt
import math
import Graph
import networkx as nx # This is for creating graphs
from prettytable import PrettyTable #Will use this for creating tables in Option 2.
nx.draw_networkx(Graph.HNetwork,with_labels=True,node_size=50) #This just makes an image of the graph we have with networkx.
plt.show()4
print("This program simulates Multilevel hierarchial routing with an example network.\nThis example network can be found inside the project folder.\n") #Brief Description
while True: # This will keep the program running until the user decides to quit.
    print("Please select an option.\n1.Route Packets in Network\n2.Display Routing Table\n3.List Border Gateway Routers\n4.Exit Program") #Menu print
    cmd = input() #collect user input
    if cmd == '1':
        print("Enter a source address: ")
        srcAdd = input() # User will enter source router address from example network
        print("Enter a destination address: ")
        dstAdd = input() # User will enter destination router address from example network
        print(nx.dijkstra_path(Graph.HNetwork, srcAdd, dstAdd))
        print ("This path takes a total of ", nx.shortest_path_length(Graph.HNetwork, srcAdd, dstAdd, weight= 'weight'), " hop(s).")
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
