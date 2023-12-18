import networkx as nx
import matplotlib.pyplot as plt
G=nx.MultiGraph ([(1,1),(1,2),(1,2),(1,4),(2,3),(2,3),(2,3),(3,3),(3,4)])
pos = nx.spring_layout(G,seed=1)
nx.draw_networkx(G, pos, node_color = 'r', node_size = 200, alpha = 1,with_labels=True)
ax = plt.gca()
for e in G.edges:
    ax.annotate("",
                xy=pos[e[0]], xycoords='data',
                xytext=pos[e[1]], textcoords='data',
                arrowprops=dict(arrowstyle="-", color="0.5",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])
                                ),
                                ),
                )
plt.axis('off')
plt.show()