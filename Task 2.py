import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def kruskals_mst(graph):
    edges = []
    for node1 in graph:
        for node2, weight in graph[node1].items():
            edges.append((weight, node1, node2))
    edges.sort()

    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    mst = []
    for weight, node1, node2 in edges:
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append((node1, node2, weight))
            yield mst  # Yield the intermediate MST for animation

# Depict graph
graph = {
    'A': {'B': 2, 'C': 7, 'D': 3},
    'B': {'A': 2, 'D': 1, 'E': 5},
    'C': {'A': 7, 'D': 3, 'F': 10},
    'D': {'A': 3, 'B': 1, 'C': 3, 'E': 6, 'F': 4, 'Z': 3},
    'E': {'B': 5, 'D': 6, 'Z': 3},
    'F': {'C': 10, 'D': 4, 'Z': 3},
    'Z': {'D': 3, 'E': 3, 'F': 3}
}

# Create the figure and axes for the plot
fig, ax = plt.subplots()

# Create the Task 2 graph
G = nx.Graph()
for node in graph:
    for neighbor, weight in graph[node].items():
        G.add_edge(node, neighbor, weight=weight)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        font_weight='bold', ax=ax)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G,
                                                                       'weight'),
                             ax=ax)

# Initialise the MST edges
mst_edges = []

# Define the animation function
def animate(mst_edges):
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            font_weight='bold', ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G,
                                                                           'weight'),
                                 ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='red',
                           width=2, ax=ax)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=kruskals_mst(graph),
                              interval=1000, repeat=False)

# Show the animation
plt.show()

#Depict the final tree

# Final MST edges 
final_mst = list(kruskals_mst(graph))[-1]  # Get the last yielded MST frame

# Show only the edges for the final MST
mst_edges = [(edge[0], edge[1]) for edge in final_mst]

# Show only the MST edges
plt.figure(figsize=(7, 5))
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='pink', width=2)

plt.title("Task 2 Minimum Spanning Tree (MST)")
plt.show()

