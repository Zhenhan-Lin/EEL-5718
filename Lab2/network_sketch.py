import networkx as nx
import matplotlib.pyplot as plt


# Create Mesh Topology figure
G_mesh = nx.Graph()

# Adding nodes
switches = ['s1', 's2', 's3', 's4']
hosts = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']

G_mesh.add_nodes_from(switches)
G_mesh.add_nodes_from(hosts)

# Adding links
# Interconnecting switches
for i, switch in enumerate(switches):
    for j in range(i + 1, len(switches)):
        G_mesh.add_edge(switch, switches[j])

# Connecting hosts to switches
for i, host in enumerate(hosts):
    G_mesh.add_edge(host, switches[i // 2])

# Drawing the topology using nx.draw_networkx
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G_mesh)
nx.draw_networkx_nodes(G_mesh, pos, nodelist=switches, node_size=2000, node_color="skyblue", node_shape='s')
nx.draw_networkx_nodes(G_mesh, pos, nodelist=hosts, node_size=2000, node_color="lightgreen", node_shape='o')
nx.draw_networkx_edges(G_mesh, pos)
nx.draw_networkx_labels(G_mesh, pos)
plt.title("Mesh Topology", fontsize=16, fontweight='bold', fontstyle='italic', color='darkred', y=1.02)
plt.axis("off")  # Hide the axis
plt.savefig("Mesh_Topology.png")


# Create Linear Topology figure
G_linear = nx.Graph()

# Adding nodes (switches and hosts are already defined)
G_linear.add_nodes_from(switches)
G_linear.add_nodes_from(hosts)

# Adding links
# Interconnecting switches in a linear fashion
for i in range(len(switches) - 1):
    G_linear.add_edge(switches[i], switches[i + 1])

# Connecting hosts to switches
for i, host in enumerate(hosts):
    G_linear.add_edge(host, switches[i // 2])

# Drawing the topology
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G_linear)
nx.draw_networkx_nodes(G_linear, pos, nodelist=switches, node_size=2000, node_color="skyblue", node_shape='s')
nx.draw_networkx_nodes(G_linear, pos, nodelist=hosts, node_size=2000, node_color="lightgreen", node_shape='o')
nx.draw_networkx_edges(G_linear, pos)
nx.draw_networkx_labels(G_linear, pos)
plt.title("Linear Topology", fontsize=16, fontweight='bold', fontstyle='italic', color='darkred', y=1.02)
plt.axis("off")  # Hide the axis
plt.savefig("Linear_Topology.png")

# Redraw Tree Topology figure with the corrected structure again
G_tree = nx.Graph()
switches.extend(['s5', 's6', 's7'])

# Adding nodes (switches and hosts are already defined)
G_tree.add_nodes_from(switches)
G_tree.add_nodes_from(hosts)

# Adding links between switches for tree topology
G_tree.add_edge('s1', 's2')
G_tree.add_edge('s1', 's3')
G_tree.add_edge('s2', 's4')
G_tree.add_edge('s2', 's5')
G_tree.add_edge('s3', 's6')
G_tree.add_edge('s3', 's7')

# Connecting hosts to switches
for i in range(3, 7):
    G_tree.add_edge(switches[i], hosts[2*i-6])
    G_tree.add_edge(switches[i], hosts[2*i-5])

# Drawing the corrected topology
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G_tree)
nx.draw_networkx_nodes(G_tree, pos, nodelist=switches, node_size=1300, node_color="skyblue", node_shape='s')
nx.draw_networkx_nodes(G_tree, pos, nodelist=hosts, node_size=1300, node_color="lightgreen", node_shape='o')
nx.draw_networkx_edges(G_tree, pos)
nx.draw_networkx_labels(G_tree, pos)
plt.title("Tree Topology", fontsize=16, fontweight='bold', fontstyle='italic', color='darkred', y=1.02)
plt.axis("off")  # Hide the axis
plt.savefig("Tree_Topology.png")
