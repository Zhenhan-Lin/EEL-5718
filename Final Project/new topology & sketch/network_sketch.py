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


# Create Star Topology figure
G_star = nx.Graph()
switches_star = 's1'
hosts_star = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12']
# Adding nodes (switches and hosts are already defined)
G_star.add_nodes_from(switches_star)
G_star.add_nodes_from(hosts_star)

for i in range(len(hosts_star)):
    G_star.add_edge(hosts_star[i], switches_star)

# Drawing the corrected topology
plt.figure(figsize=(8, 8))
pos = nx.spring_layout(G_star)
nx.draw_networkx_nodes(G_star, pos, nodelist=[switches_star], node_size=2500, node_color="skyblue", node_shape='s')
nx.draw_networkx_nodes(G_star, pos, nodelist=hosts_star, node_size=2500, node_color="lightgreen", node_shape='o')
nx.draw_networkx_edges(G_star, pos)
nx.draw_networkx_labels(G_star, pos)
plt.title("Star Topology", fontsize=16, fontweight='bold', fontstyle='italic', color='darkred', y=1.02)
plt.axis("off")  # Hide the axis
plt.savefig("Star_Topology.png")

# Create Ring Topology figure
G_ring = nx.Graph()
switches_ring = ['s1', 's2', 's3', 's4', 's5', 's6']
hosts_ring = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
# Adding nodes (switches and hosts are already defined)
G_ring.add_nodes_from(switches_ring)
G_ring.add_nodes_from(hosts_ring)

for i in range(len(hosts_ring)):
    G_ring.add_edge(hosts_ring[i], switches_ring[i])

for i in range(len(switches_ring)-1):
    G_ring.add_edge(switches_ring[i], switches_ring[i+1])

G_ring.add_edge(switches_ring[0], switches_ring[-1])
# Drawing the corrected topology
plt.figure(figsize=(7, 7))
pos = nx.spring_layout(G_ring)
nx.draw_networkx_nodes(G_ring, pos, nodelist=switches_ring, node_size=1300, node_color="skyblue", node_shape='s')
nx.draw_networkx_nodes(G_ring, pos, nodelist=hosts_ring, node_size=1300, node_color="lightgreen", node_shape='o')
nx.draw_networkx_edges(G_ring, pos)
nx.draw_networkx_labels(G_ring, pos)
plt.title("Ring Topology", fontsize=16, fontweight='bold', fontstyle='italic', color='darkred', y=1.02)
plt.axis("off")  # Hide the axis
plt.savefig("Ring_Topology.png")

# Create Hybrid Topology figure
G_hyb = nx.Graph()
switches_hyb = ['s1', 's2', 's3', 's4', 's5', 's6', 's7']
hosts_hyb = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
# Adding nodes (switches and hosts are already defined)
G_hyb.add_nodes_from(switches_hyb)
G_hyb.add_nodes_from(hosts_hyb)

G_hyb.add_edge(switches_hyb[0], switches_hyb[1])
G_hyb.add_edge(switches_hyb[0], switches_hyb[2])
G_hyb.add_edge(switches_hyb[1], switches_hyb[2])  # First ring
G_hyb.add_edge(switches_hyb[1], switches_hyb[3])
G_hyb.add_edge(switches_hyb[1], switches_hyb[4])
G_hyb.add_edge(switches_hyb[3], switches_hyb[4])  # Second ring
G_hyb.add_edge(switches_hyb[2], switches_hyb[5])
G_hyb.add_edge(switches_hyb[2], switches_hyb[6])
G_hyb.add_edge(switches_hyb[5], switches_hyb[6])  # Third ring
G_hyb.add_edge(switches_hyb[3], hosts_hyb[0])
G_hyb.add_edge(switches_hyb[3], hosts_hyb[1])
G_hyb.add_edge(switches_hyb[4], hosts_hyb[2])
G_hyb.add_edge(switches_hyb[4], hosts_hyb[3])
G_hyb.add_edge(switches_hyb[5], hosts_hyb[4])
G_hyb.add_edge(switches_hyb[5], hosts_hyb[5])
G_hyb.add_edge(switches_hyb[6], hosts_hyb[6])
G_hyb.add_edge(switches_hyb[6], hosts_hyb[7])

# Drawing the corrected topology
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G_hyb)
nx.draw_networkx_nodes(G_hyb, pos, nodelist=switches_hyb, node_size=1100, node_color="skyblue", node_shape='s')
nx.draw_networkx_nodes(G_hyb, pos, nodelist=hosts_hyb, node_size=1100, node_color="lightgreen", node_shape='o')
nx.draw_networkx_edges(G_hyb, pos)
nx.draw_networkx_labels(G_hyb, pos)
plt.title("Hybrid Topology", fontsize=16, fontweight='bold', fontstyle='italic', color='darkred', y=1.02)
plt.axis("off")  # Hide the axis
plt.savefig("Hybrid_Topology.png")


