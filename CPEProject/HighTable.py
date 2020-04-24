
from __main__ import *
import matplotlib.pyplot as plt
import math
import Graph
import networkx as nx 
from prettytable import PrettyTable

x = PrettyTable()
i = 0
nextAdd = list(Graph.HNetwork.neighbors(rtrAdd)) # nextAdd represents the next address, or the next hop of the inputted address
nextAddCount = len(nextAdd) # nextAddCount represents the amount of hops it takes to get to the neighbor
x.field_names = ["Destination", "Line", "Weight"]
for y in range(nextAddCount):
    j = 0
    weight = nx.dijkstra_path_length(Graph.HNetwork, rtrAdd, nextAdd[i]) # weight is the amount of hops it takes to get from the inputted address to the next address in the array of addresses
    line = nx.dijkstra_path(Graph.HNetwork, rtrAdd, nextAdd[i]) # line represents the next hop to take after the inputted address
    try:
        x.add_row([nextAdd[i], line[1], weight])
    except IndexError:
        pass
    i = i + 1
