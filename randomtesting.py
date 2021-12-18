
from generallibrary import *

import matplotlib.pyplot as plt
import networkx as nx

from generalpackager import Packager

# create a directed multi-graph
G = nx.DiGraph()

for package in Packager().get_all():
    for dependant in package.get_children():
        G.add_edge(package.simple_name, dependant.simple_name)


# plot the graph
plt.figure(figsize=(8, 8))
nx.draw(G, pos=nx.circular_layout(G), connectionstyle='arc3, rad=-0.1', with_labels=True, node_color="None", node_size=3000, node_shape="s")

plt.show()  # pause before exiting



