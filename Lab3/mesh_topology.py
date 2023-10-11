from mininet.topo import Topo
from mininet.node import OVSBridge


class Mesh_Topo(Topo):
    """
        Mesh topology example.
    """
    def __init__(self):
        """
            Create mesh topo.
        """
        # Initialize topology
        super().__init__()

        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')

        s1 = self.addSwitch('s1', cls=OVSBridge, stp=True)
        s2 = self.addSwitch('s2', cls=OVSBridge, stp=True)
        s3 = self.addSwitch('s3', cls=OVSBridge, stp=True)
        s4 = self.addSwitch('s4', cls=OVSBridge, stp=True)

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(s1, s2)
        self.addLink(s2, h3)
        self.addLink(s2, h4)
        self.addLink(s1, s3)
        self.addLink(s3, h5)
        self.addLink(s3, h6)
        self.addLink(s1, s4)
        self.addLink(s4, h7)
        self.addLink(s4, h8)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s3, s4)


topos = {'mesh_topo': (lambda: Mesh_Topo())}
