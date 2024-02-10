import networkx as nx
import matplotlib
import matplotlib.pyplot


class Network:

    def __init__(self):
        self.network = nx.MultiDiGraph()

    def add_edges(self, src, dest: list):
        for x in dest:
            self.network.add_edge(src, x)

    def save_image(self, filename):
        fig = matplotlib.pyplot.figure()
        nx.draw(self.network, ax=fig.add_subplot(), labels={node: node for node in self.network.nodes()})
        matplotlib.use("Agg")
        fig.savefig(f"{filename}.png")

    def clear(self):
        self.network.clear()
