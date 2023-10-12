## EEL5718 Lab-2 Code

### Command & Test

+ To run any test, please open terminal under this folder
+ For starting mesh/lineear/tree topology, run code below:
```angular2html
sudo mn --custom mesh_topology.py --topo mesh_topo
sudo mn --custom linear_topology.py --topo linear_topo
sudo mn --custom tree_topology.py --topo treee_topo
```
+ For doing conduct pingall tests and latency experiments, please run code below
```
mininet> pingall
mininet> xterm h1
mininet> xterm h3

===== In the terminal of h1 and h3 =====

host 1 > qperf

host 3 > qperf -vvs 10.0.0.1 tcp_lat
host 3 > qperf -vvs 10.0.0.1 udp_lat
```
Notice that the `pingall` test work should be down 30s after starting mesh topology since STP needs time. And all the test work screenshots are included in the folder ./result

### Introduction of topologies
+ Mesh topology
The mesh topology includes 4 switches (mesh connection) and 8 hosts. Each switch connects to two hosts. Since mesh connection forms loop in the network, we set `stp=True` and `cls=OVSBridge` for switches to utilize the Spanning Tree Protocol to find the shortest route for connection between hosts and make `ping` test successful. 
![alt text](https://github.com/Zhenhan-Lin/EEL-5718/blob/main/Lab3/figure/Mesh_Topology.png)
+ Linear topology
The mesh topology includes 4 switches (linear connection) and 8 hosts. Each switch connects to two hosts.
![alt text](https://github.com/Zhenhan-Lin/EEL-5718/blob/main/Lab3/figure/Linear_Topology.png)
+ Tree topology
The mesh topology includes 7 switches (tree connection) and 8 hosts. The switch tree has three layers. The first layer includes root node and the last layer includes 4 leaves of the tree. Each leaf switch connects to two hosts.
![alt text](https://github.com/Zhenhan-Lin/EEL-5718/blob/main/Lab3/figure/Tree_Topology.png)
