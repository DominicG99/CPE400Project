from __main__ import *
import matplotlib.pyplot as plt
import math
import Graph
import networkx as nx 
from prettytable import PrettyTable
x = PrettyTable()
Dict = {} #Dict is used to get shortest path to region or cluster.
count = 1 #using this to display how many entries are in the table.
#allAdd represents all addresses; it contains every node address in the graph
allAdd = list(Graph.HNetwork)
allAdd.sort()
#settings the column names.
x.field_names = ["Destination", "Line", "Weight"]
#adding to initial row of the inputted router address.
x.add_row([rtrAdd, '---', '---'])
for i in range(len(allAdd)):
    #Check if in the same cluster
    if(Graph.nodeAttributes[rtrAdd]['Cluster'] == Graph.nodeAttributes[allAdd[i]]['Cluster']):
        #If in the same cluster, check if in the same region
        if(Graph.nodeAttributes[rtrAdd]['Region'] == Graph.nodeAttributes[allAdd[i]]['Region']):
            #If in the same cluster and region
            #weight is the amount of hops it takes to get from the inputted address to the next address in the array of addresses
            weight = nx.dijkstra_path_length(Graph.HNetwork, rtrAdd, allAdd[i])
            #line represents the next hop to take after the inputted address
            line = nx.dijkstra_path(Graph.HNetwork, rtrAdd, allAdd[i])
            try:
                x.add_row([allAdd[i], line[1], weight]) #adding row
                count += 1
            except IndexError:
                pass
        else: #In the same cluster, but not in the same region
            #Setting destination to use for dictionary.
            destination = "Region " + str(Graph.nodeAttributes[allAdd[i]]['Region'])
            if destination in Dict:
                #Compare weight with existing keys value
                if Dict[destination] > nx.dijkstra_path_length(Graph.HNetwork, rtrAdd, allAdd[i]):
                    #if the weight of node to region is more than what is inputted, change to lesser weight
                    Dict[destination] = nx.dijkstra_path_length(Graph.HNetwork, rtrAdd, allAdd[i])
                    #keeping tracking of the line it takes.
                    line = nx.dijkstra_path(Graph.HNetwork, rtrAdd, allAdd[i])
            else:
                #If key doesnt exist yet, add it
                Dict[destination] = nx.dijkstra_path_length(Graph.HNetwork, rtrAdd, allAdd[i])
    else: #Not in the same cluster
        #Setting destination to use for dictionary.
        destination = "Cluster " + str(Graph.nodeAttributes[allAdd[i]]['Cluster'])
        if destination in Dict: #checking if the cluster already exists in dictionary
            #Compare weight with existing keys value
            if Dict[destination] > nx.dijkstra_path_length(Graph.HNetwork, rtrAdd, allAdd[i]):
                #if the weight of node tocluster is more than what is inputted, change to lesser weight
                Dict[destination] = nx.dijkstra_path_length(Graph.HNetwork, rtrAdd, allAdd[i])
                #keeping tracking of the line it takes.
                line = nx.dijkstra_path(Graph.HNetwork, rtrAdd, allAdd[i])
        else:
            #If key doesnt exist yet, add it
            Dict[destination] = nx.dijkstra_path_length(Graph.HNetwork, rtrAdd, allAdd[i])
            weight = nx.dijkstra_path_length(Graph.HNetwork, rtrAdd, allAdd[i])
#Construct the table with Dictionary keys.
for key, value in Dict.items():
    x.add_row([key, line[1], value])
    count += 1