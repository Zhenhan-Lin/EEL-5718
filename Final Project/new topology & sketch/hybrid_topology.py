from mininet.topo import Topo
from mininet.node import OVSBridge

class Hybrid_Topo(Topo):
    """
        Hybrid topology example.
    """

    def __init__(self):
        """
            Create hybrid topo.
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
        s5 = self.addSwitch('s5', cls=OVSBridge, stp=True)
        s6 = self.addSwitch('s6', cls=OVSBridge, stp=True)
        s7 = self.addSwitch('s7', cls=OVSBridge, stp=True)

        # Add links
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s2, s3)  # First ring
        self.addLink(s2, s4)
        self.addLink(s2, s5)
        self.addLink(s4, s5)  # Second ring
        self.addLink(s3, s6)
        self.addLink(s3, s7)
        self.addLink(s6, s7)  # Third ring
        self.addLink(s4, h1)
        self.addLink(s4, h2)
        self.addLink(s5, h3)
        self.addLink(s5, h4)
        self.addLink(s6, h5)
        self.addLink(s6, h6)
        self.addLink(s7, h7)
        self.addLink(s7, h8)


topos = {'hybrid_topo': (lambda: Hybrid_Topo())}