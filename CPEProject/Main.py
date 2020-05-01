# Authors: Dominic Ginter, Cole Atkinson, Kelly Tay
# CPE 400 Project
# Hierarchial Routing Simulation

import matplotlib.pyplot as plt
import math
import Graph
from PIL import Image
import networkx as nx # This is for creating graphs
from prettytable import PrettyTable #Will use this for creating tables in Option 2.
import imp
impTableCount = 0 #Helps reimport files
impHighTableCount = 0 #Helps reimport files
print("This program simulates Multilevel hierarchial routing with an example network.\n \
        This example network can be found by selecting option 4.\n") #Brief Description

while True: # This will keep the program running until the user decides to quit.
    #Menu print
    print("Please select an option.\n \
            1.Route Packets in Network\n \
            2.Display Routing Table\n \
            3.Display Mathematical Nodal map\n \
            4.Display Realistic Nodal map \n \
            5.Exit program")
    cmd = input() #collect user input
    
    if cmd == '1': #Option 1
        print("Enter a source address: ")
        srcAdd = input() # User will enter source router address from example network
        print("Enter a destination address: ")
        dstAdd = input() # User will enter destination router address from example network
        print(nx.dijkstra_path(Graph.HNetwork, srcAdd, dstAdd))
        print ("This path takes a total of ",
            nx.shortest_path_length(Graph.HNetwork, srcAdd, dstAdd, weight= 'weight'), "hop(s).")
    elif cmd == '2': #Option 2
        print("Enter a router address: ") # User will enter a router address from example network
        rtrAdd = input()
        #This will show the difference between full table and hierarchial table
        print("Please select a routing table display option.\n \
                1.Full Table\n \
                2.Hierarchial Table")
        tableChoice = input() # Get input
        if tableChoice == '1':
            import Table
            impTableCount = impHighTableCount + 1 #increment import variable
            if impTableCount >= 1: #File has already been imported
                imp.reload(Table) #Reset Import
            print(Table.x)
            # Will print the full routing table here
        elif tableChoice == '2':
            import HighTable #Hierarchial table file
            impHighTableCount = impHighTableCount + 1 #increment import variable
            if impHighTableCount >= 1: #File has already been imported
                imp.reload(HighTable) #Reset Import
            print(HighTable.x, "\nThis table has", 37 - HighTable.count, "less entries than the full table.")
            print("Memory Efficieny:", 100 - (HighTable.count / 37) * 100, "%")
            # Will print the hierarchial routing table here
    elif cmd == '3': # Option 3
        #This just makes an image of the graph we have with networkx.
        nx.draw_networkx(Graph.HNetwork,
        with_labels=True,node_size=80, font_size = 8, fontweight = 'bold', figsize = (60, 60))
        print("Displaying the mathematical nodal map...")
        plt.show() # Opens the Nodal Map
    elif cmd == '4': # Option 4
        print("Displaying the realistic nodal map")
        realisticImage = Image.open('Example network.jpg') #Opens the example network image
        realisticImage.show() # Displays the example network image
    elif cmd == '5': # Exit
        break
    