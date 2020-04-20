try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx

G=nx.Graph()
G = nx.MultiGraph()
G.add_nodes_from([0,36])
G.add_edges_from([(0,1),(0,3),(1,2),(2,3)], weight = 1.0)
G.add_edges_from([(4,5),(4,7), (5,6), (6,7)], weight = 1.0)
G.add_edges_from([(8,9),(8,10),(9,10)], weight = 2.0) #Cluster 1 Region 3 Connections
G.add_edge(2,9, weight = 9.0)
G.add_edge(2,7, weight = 8.0)
print(nx.dijkstra_path(G,0,4))
elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]

pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=700)

# edges
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=6)
nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=6,alpha=0.5,edge_color='b',style='dashed')

# labels
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show() # display
circle1 = plt.Circle((0, 0), 0.2, color='r')
circle2 = plt.Circle((0.5, 0.5), 0.2, color='blue')
circle3 = plt.Circle((1, 1), 0.2, color='g', clip_on=False)

fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)

fig.savefig('plotcircles.png')