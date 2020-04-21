from __main__ import *
import matplotlib.pyplot as plt
import math
import Graph
import networkx as nx 
from prettytable import PrettyTable
x = PrettyTable()
nextAdd = Graph.HNetwork.neighbors(rtrAdd) #This is necessary for the next hop address, but it displays a whack ass error
x.field_names = ["Destination", "Line", "Weight"]
print(x)
