from mininet.topo import Topo


class Star_Topo(Topo):
    """
        Star topology example.
    """

    def __init__(self):
        """
            Create star topo.
        """
        # Initialize topology
        super().__init__()

        # Add hosts and switches
        s1 = self.addSwitch('s1')
        hosts = [self.addHost(f'h{i}') for i in range(1, 13)]
        for h in hosts:
            self.addLink(s1, h)


topos = {'star_topo': (lambda: Star_Topo())}