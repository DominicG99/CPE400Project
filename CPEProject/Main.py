# Authors: Dominic Ginter, <Insert Name 2>, <Insert Name 3>
# CPE 400 Project
# Hierarchial Routing Simulation
import matplotlib.pyplot as plt
import math
import networkx as nx # This is for creating graphs
C1R1 = nx.MultiGraph() #Cluster 1 Region 1 Nodes
C1R2 = nx.MultiGraph() #Cluster 1 Region 2 Nodes
C1R3 = nx.MultiGraph() #Cluster 1 Region 3 Nodes
C2R1 = nx.MultiGraph() #Cluster 2 Region 2 Nodes
C2R2 = nx.MultiGraph() #Cluster 2 Region 2 Nodes
C2R3 = nx.MultiGraph() #Cluster 2 Region 3 Nodes
C2R4 = nx.MultiGraph() #Cluster 2 Region 4 Nodes
C3R1 = nx.MultiGraph()
C3R2 = nx.MultiGraph()
C1R1.add_nodes_from([1,4]) #Creating Nodes
C1R2.add_nodes_from([1,4])
C1R3.add_nodes_from([1,4])
C2R1.add_nodes_from([1,5])
C2R2.add_nodes_from([1,4])
C2R3.add_nodes_from([1,4])
C2R4.add_nodes_from([1,4])
C1R1.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1) #Adding Edges
C1R2.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1) #Adding Edges
C1R3.add_edges_from([(1,2),(1,3),(2,3)], weight = 2.0) #Adding Edges
C1R3.add_edge(2,4, weight = 3)
C2R1.add_edges_from([(2,3), (2,5), (3,4), (4,5)], weight = 1)
C2R1.add_edge(1,2, weight = 2)
C2R2.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1)
C2R3.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1)
C2R4.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1)
C3R1.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1)
C3R2.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1)
Cluster1 = nx.union(C1R1,C1R2, rename=('1.1.', '1.2.'))
Cluster1 = nx.union(Cluster1, C1R3, rename=('','1.3.'))
Cluster2 = nx.union(C2R1, C2R2, rename=('2.1.', '2.2.'))
Cluster2 = nx.union(Cluster2, C2R3, rename=('', '2.3.'))
Cluster2 = nx.union(Cluster2, C2R4, rename=('', '2.4.'))
Cluster3 = nx.union(C3R1, C3R2, rename=('3.1.', '3.2.'))
Cluster1 = nx.union(Cluster1, Cluster2)
Cluster1.add_edge('1.1.3', '1.2.4', weight = 4)
Cluster1.add_edge('1.1.3', '1.3.2', weight = 9)
Cluster1.add_edge('1.2.4', '1.3.2', weight = 8)
Cluster1.add_edge('1.3.4', '2.1.1', weight = 14)
Cluster1.add_edge('2.1.3', '2.2.1', weight = 6)
Cluster1.add_edge('2.1.5', '2.4.1', weight = 4)
Cluster1.add_edge('2.4.3', '2.3.4', weight = 7)
HNetwork = nx.union(Cluster1, Cluster3)
HNetwork.add_edge('3.1.3', '3.2.4', weight = 3)
HNetwork.add_edge('3.2.1', '2.4.4', weight = 14)
HNetwork.add_edge('3.1.1', '1.3.4', weight = 12)
nx.draw_networkx(HNetwork,with_labels=True,node_size=50)
plt.show()
print(nx.dijkstra_path(HNetwork,'1.1.1','2.3.2'))
print("This program simulates Multilevel hierarchial routing with an example network.\nThis example network can be found inside the project folder.\n") #Brief Description
while True: # This will keep the program running until the user decides to quit.
    print("Please select an option.\n1.Route Packets in Network\n2.Display Routing Table\n3.List Border Gateway Routers\n4.Exit Program") #Menu print
    cmd = input() #collect user input
    if cmd == '1':
        print("Enter a source address: ")
        srcAdd = input() # User will enter source router address from example network
        print("Enter a destination address: ")
        dstAdd = input() # User will enter destination router address from example network
        print(nx.dijkstra_path(HNetwork, srcAdd, dstAdd))
        print("This path takes a total of ")
        print(nx.shortest_path_length(HNetwork, srcAdd, dstAdd, weight= 'weight'))
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
