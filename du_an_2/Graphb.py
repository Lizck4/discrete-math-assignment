import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
n = 5
random.seed(1)
matrix = [[random.randint(1,100) for j in range(n)] for i in range(n)]
for i in range(n):
    matrix[i][i] = 0
print(matrix)

# # Weighted matrix representing the graph
# matrix = [
#     [0, 73, 98, 9, 33],
#     [16, 0, 98, 58, 61],
#     [84, 49, 0, 13, 63],
#     [4, 50, 56, 0, 98],
#     [99, 1, 90, 58, 0]
# ]

# Create a graph from the weighted matrix
G = nx.Graph()
num_nodes = len(matrix)
G.add_nodes_from(range(num_nodes))
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        weight = matrix[i][j]
        if weight > 0:
            G.add_edge(i, j, weight=weight)

# Draw the graph

pos = nx.spring_layout(G,seed=34)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the graph
plt.show()
