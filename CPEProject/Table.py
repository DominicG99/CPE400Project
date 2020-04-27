
from __main__ import *
import matplotlib.pyplot as plt
import math
import Graph
import networkx as nx 
from prettytable import PrettyTable
x = PrettyTable()

#allAdd represents all addresses; it contains every node address in the graph
allAdd = list(Graph.HNetwork)
allAdd.sort()
x.field_names = ["Destination", "Line", "Weight"]
x.add_row([rtrAdd, '---', '---'])
for i in range(len(allAdd)) :
    #weight is the amount of hops it takes to get from the inputted address
    #to the next address in the array of addresses
    weight = nx.dijkstra_path_length(Graph.HNetwork, rtrAdd, allAdd[i])
    #line represents the next hop to take after the inputted address
    line = nx.dijkstra_path(Graph.HNetwork, rtrAdd, allAdd[i])
    try:
        #Add row
        x.add_row([allAdd[i], line[1], weight])
    except IndexError:
        pass