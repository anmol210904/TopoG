import bfs
import networkx as nx
import matplotlib.pyplot as plt

while(True):
    graph = bfs.bfs("1.1.1.1")

    nx.draw(graph, with_labels=True, node_color='skyblue', node_size=1500, font_size=16, font_color='black', edge_color='gray')

    plt.title("Network Graph Example")
    plt.show()

