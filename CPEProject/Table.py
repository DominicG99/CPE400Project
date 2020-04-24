
from __main__ import *
import matplotlib.pyplot as plt
import math
import Graph
import networkx as nx 
from prettytable import PrettyTable
x = PrettyTable()
i = 0
j = 0
allAdd = list(Graph.HNetwork)
x.field_names = ["Destination", "Line", "Weight"]
for y in range(len(allAdd)) :
    j = 0
    weight = nx.dijkstra_path_length(Graph.HNetwork, rtrAdd, allAdd[i])
    rude = nx.dijkstra_path(Graph.HNetwork, rtrAdd, allAdd[i])
    try:
        x.add_row([allAdd[i], rude[1], weight])
    except IndexError:
        pass
    i = i + 1