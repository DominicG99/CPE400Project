import networkx as nx # This is for creating graphs

C1R1 = nx.MultiGraph() #Cluster 1 Region 1 Nodes
C1R2 = nx.MultiGraph() #Cluster 1 Region 2 Nodes
C1R3 = nx.MultiGraph() #Cluster 1 Region 3 Nodes
C2R1 = nx.MultiGraph() #Cluster 2 Region 1 Nodes
C2R2 = nx.MultiGraph() #Cluster 2 Region 2 Nodes
C2R3 = nx.MultiGraph() #Cluster 2 Region 3 Nodes
C2R4 = nx.MultiGraph() #Cluster 2 Region 4 Nodes
C3R1 = nx.MultiGraph() #Cluster 3 Region 1 Nodes
C3R2 = nx.MultiGraph() #Cluster 3 Region 2 Nodes

#Creating Nodes
C1R1.add_nodes_from([1,4])
C1R2.add_nodes_from([1,4])
C1R3.add_nodes_from([1,4])
C2R1.add_nodes_from([1,5])
C2R2.add_nodes_from([1,4])
C2R3.add_nodes_from([1,4])
C2R4.add_nodes_from([1,4])
C3R1.add_nodes_from([1,4])
C3R2.add_nodes_from([1,4])

#Setting Node Attributes
nodeAttributes = {'1.1.1': {'Cluster': 1, 'Region': 1, 'Node':1}, 
                '1.1.2': {'Cluster': 1, 'Region': 1, 'Node':2},
                '1.1.3': {'Cluster': 1, 'Region': 1, 'Node':3},
                '1.1.4': {'Cluster': 1, 'Region': 1, 'Node':4},
                '1.2.1': {'Cluster': 1, 'Region': 2, 'Node':1}, 
                '1.2.2': {'Cluster': 1, 'Region': 2, 'Node':2},
                '1.2.3': {'Cluster': 1, 'Region': 2, 'Node':3},
                '1.2.4': {'Cluster': 1, 'Region': 2, 'Node':4},
                '1.3.1': {'Cluster': 1, 'Region': 3, 'Node':1}, 
                '1.3.2': {'Cluster': 1, 'Region': 3, 'Node':2},
                '1.3.3': {'Cluster': 1, 'Region': 3, 'Node':3},
                '1.3.4': {'Cluster': 1, 'Region': 3, 'Node':4},
                '2.1.1': {'Cluster': 2, 'Region': 1, 'Node':1}, 
                '2.1.2': {'Cluster': 2, 'Region': 1, 'Node':2},
                '2.1.3': {'Cluster': 2, 'Region': 1, 'Node':3},
                '2.1.4': {'Cluster': 2, 'Region': 1, 'Node':4},
                '2.1.5': {'Cluster': 2, 'Region': 1, 'Node':5},
                '2.2.1': {'Cluster': 2, 'Region': 2, 'Node':1}, 
                '2.2.2': {'Cluster': 2, 'Region': 2, 'Node':2},
                '2.2.3': {'Cluster': 2, 'Region': 2, 'Node':3},
                '2.2.4': {'Cluster': 2, 'Region': 2, 'Node':4},
                '2.3.1': {'Cluster': 2, 'Region': 3, 'Node':1}, 
                '2.3.2': {'Cluster': 2, 'Region': 3, 'Node':2},
                '2.3.3': {'Cluster': 2, 'Region': 3, 'Node':3},
                '2.3.4': {'Cluster': 2, 'Region': 3, 'Node':4},
                '2.4.1': {'Cluster': 2, 'Region': 4, 'Node':1}, 
                '2.4.2': {'Cluster': 2, 'Region': 4, 'Node':2},
                '2.4.3': {'Cluster': 2, 'Region': 4, 'Node':3},
                '2.4.4': {'Cluster': 2, 'Region': 4, 'Node':4},
                '3.1.1': {'Cluster': 3, 'Region': 1, 'Node':1}, 
                '3.1.2': {'Cluster': 3, 'Region': 1, 'Node':2},
                '3.1.3': {'Cluster': 3, 'Region': 1, 'Node':3},
                '3.1.4': {'Cluster': 3, 'Region': 1, 'Node':4},
                '3.2.1': {'Cluster': 3, 'Region': 2, 'Node':1}, 
                '3.2.2': {'Cluster': 3, 'Region': 2, 'Node':2},
                '3.2.3': {'Cluster': 3, 'Region': 2, 'Node':3},
                '3.2.4': {'Cluster': 3, 'Region': 2, 'Node':4}}

#Adding Edges between nodes
C1R1.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1)
C1R2.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1)
C1R3.add_edges_from([(1,2),(1,3),(2,3)], weight = 2)
C1R3.add_edge(2,4, weight = 3)
C2R1.add_edges_from([(2,3), (2,5), (3,4), (4,5)], weight = 1)
C2R1.add_edge(1,2, weight = 2)
C2R2.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1)
C2R3.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1)
C2R4.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1)
C3R1.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1)
C3R2.add_edges_from([(1,2),(1,4),(2,3),(3,4)], weight = 1)
Cluster1 = nx.union(C1R1,C1R2, rename=('1.1.', '1.2.'))
Cluster1 = nx.union(Cluster1, C1R3, rename=('','1.3.'))
Cluster2 = nx.union(C2R1, C2R2, rename=('2.1.', '2.2.'))
Cluster2 = nx.union(Cluster2, C2R3, rename=('', '2.3.'))
Cluster2 = nx.union(Cluster2, C2R4, rename=('', '2.4.'))
Cluster3 = nx.union(C3R1, C3R2, rename=('3.1.', '3.2.'))
Cluster1 = nx.union(Cluster1, Cluster2)
Cluster1.add_edge('1.1.3', '1.2.4', weight = 4)
Cluster1.add_edge('1.1.3', '1.3.2', weight = 9)
Cluster1.add_edge('1.2.4', '1.3.2', weight = 8)
Cluster1.add_edge('1.3.4', '2.1.1', weight = 14)
Cluster1.add_edge('2.1.3', '2.2.1', weight = 6)
Cluster1.add_edge('2.1.5', '2.4.1', weight = 4)
Cluster1.add_edge('2.4.3', '2.3.4', weight = 7)
HNetwork = nx.union(Cluster1, Cluster3)
HNetwork.add_edge('3.1.3', '3.2.4', weight = 3)
HNetwork.add_edge('3.2.1', '2.4.4', weight = 14)
HNetwork.add_edge('3.1.1', '1.3.4', weight = 12)