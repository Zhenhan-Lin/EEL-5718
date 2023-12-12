## EEL5718 Final Project Code

### Command & Test

+ To run the code, please open terminal under this folder
+ For starting topology, run code below:
```angular2html
sudo mn --custom mesh_topology.py --topo mesh_topo
sudo mn --custom linear_topology.py --topo linear_topo
sudo mn --custom tree_topology.py --topo tree_topo
sudo mn --custom star_topology.py --topo star_topo
sudo mn --custom hybrid_topology.py --topo hybrid_topo
sudo mn --custom ring_topology.py --topo ring_topo
```
+ For doing conduct pingall tests and latency experiments, please run code below
```
mininet> xterm h1
mininet> xterm h3

===== In the terminal of h1 and h3 =====

host 1 > python3 sctpserver.py server_ip timeout_sec timeout_sec

host 3 > python3 sctpclient.py destination_ip destination_port topology_name
host 3 > qperf -vvs 10.0.0.1 udp_lat
```
Here you can replace the file with 'protocol+server.py' and 'protocol+client.py' to run different experiments.

