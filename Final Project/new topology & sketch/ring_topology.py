from mininet.topo import Topo
from mininet.node import OVSBridge

class Ring_Topo(Topo):
    """
    Ring topology example.
"""
    def __init__(self):
        """
            Create ring topo.
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

        s1 = self.addSwitch('s1', cls=OVSBridge, stp=True)
        s2 = self.addSwitch('s2', cls=OVSBridge, stp=True)
        s3 = self.addSwitch('s3', cls=OVSBridge, stp=True)
        s4 = self.addSwitch('s4', cls=OVSBridge, stp=True)
        s5 = self.addSwitch('s5', cls=OVSBridge, stp=True)
        s6 = self.addSwitch('s6', cls=OVSBridge, stp=True)

    # Add links
    self.addLink(h1, s1)
    self.addLink(h2, s2)
    self.addLink(h3, s3)
    self.addLink(h4, s4)
    self.addLink(h5, s5)
    self.addLink(h6, s6)
    self.addLink(s1, s2)
    self.addLink(s2, s3)
    self.addLink(s3, s4)
    self.addLink(s4, s5)
    self.addLink(s5, s6)
    self.addLink(s6, s1)


topos = {'ring_topo': (lambda: Ring_Topo())}