
from __main__ import *
import matplotlib.pyplot as plt
import math
import Graph
import networkx as nx 
from prettytable import PrettyTable

x = PrettyTable()
i = 0
nextAdd = list(Graph.HNetwork.neighbors(rtrAdd))
nextAddCount = len(nextAdd)
x.field_names = ["Destination", "Line", "Weight"]
for y in range(nextAddCount):
    j = 0
    weight = nx.dijkstra_path_length(Graph.HNetwork, rtrAdd, nextAdd[i])
    rude = nx.dijkstra_path(Graph.HNetwork, rtrAdd, nextAdd[i])
    try:
        x.add_row([nextAdd[i], rude[1], weight])
    except IndexError:
        pass
    i = i + 1
