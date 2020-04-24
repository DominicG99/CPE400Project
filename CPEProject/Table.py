
from __main__ import *
import matplotlib.pyplot as plt
import math
import Graph
import networkx as nx 
from prettytable import PrettyTable
x = PrettyTable()
i = 0
j = 0
allAdd = list(Graph.HNetwork) #allAdd represents all addresses; it contains every node address in the graph
x.field_names = ["Destination", "Line", "Weight"]
for y in range(len(allAdd)) :
    j = 0
    weight = nx.dijkstra_path_length(Graph.HNetwork, rtrAdd, allAdd[i]) # weight is the amount of hops it takes to get from the inputted address to the next address in the array of addresses
    line = nx.dijkstra_path(Graph.HNetwork, rtrAdd, allAdd[i]) # line represents the next hop to take after the inputted address
    try:
        x.add_row([allAdd[i], line[1], weight])
    except IndexError:
        pass
    i = i + 1