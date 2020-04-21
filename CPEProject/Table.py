from __main__ import *
import matplotlib.pyplot as plt
import math
import Graph
import networkx as nx 
from prettytable import PrettyTable
x = PrettyTable()
nextAdd = Graph.HNetwork.neighbors(rtrAdd) #This is necessary for the next hop address, but it displays a whack ass error
x.field_names = ["Network ID", "Subnet Mask", "Next Hop", "Outgoing Interface", "Metric"]
#Network ID is the IP address being analyzed in the row of the table
#Subnet Mask is what I found online about class a ip addresses, which is what i am assuming these addresses are under since they all start with 1-3
#Next hop is the next chronological hop, not necessarily the cheapest hop
#Outgoing Interface is confusing, I am assuming it means where the IP address is located in the Example network.jpg
#Metric represents the amount of hops it takes to get to the NEXT address

#The table works as it needs to, however, Next hop is almost complete I just need to figure out how to debug the whack ass error im getting. I need to fix outgoing interface and metric

x.add_row([rtrAdd, "255.0.0.0", rtrAdd, "Cluster 1 - Region 1", "1"])

print(x)
