from collections import deque
import telnet
import loopback0
import networkx as nx
import matplotlib.pyplot as plt


def bfs(start):
    visited = set() 
    queue = deque([start])  
    
    G = nx.Graph()
    G.add_node(start)
    
    while queue:
       
        vertex = queue.popleft()
        
        if vertex not in visited:
            print(vertex)  
            visited.add(vertex)  
            G.add_node(start)
            
       
            temp_neighbours = telnet.get_cdp_neighbor_ips(vertex,"admin","admin")
            neighbour = set()
            for i in temp_neighbours:
                loopback = loopback0.get_loopback_address(i)
                if(loopback):
                    neighbour.add(loopback)
                    G.add_edge(vertex,loopback)
                
            
            for i in neighbour:
                if i not in visited:
                    queue.append(i)
                    
    return G


graph = bfs("1.1.1.1")

nx.draw(graph, with_labels=True, node_color='skyblue', node_size=1500, font_size=16, font_color='black', edge_color='gray')

plt.title("Network Graph Example")
plt.show()
