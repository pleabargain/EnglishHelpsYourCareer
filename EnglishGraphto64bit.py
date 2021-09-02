#importing the package

import networkx as nx
import matplotlib.pyplot as plt

title ="take"

#push the nodes into an array
nodes =[title, 
        "a photo",
        "a break", 
        "a walk",
        "a load off", # relax
        "my lunch break", 
        "some time off", 
        "off for\nthe weekend", # go on vacation
        "the long view", # look into the future
        "off my\nclothes", 
        "a nap", 
        "a shower", 
        "a seat",
        "a bath", 
        "a bow", # after performing  you take a bow
        "apart something", # disassemble
        "part at an event", # participate
        "a look around", # 
        "pleasure in", # enjoy
        ]

#initializing an empty graph
G = nx.Graph()
nx.add_star(G, nodes)


nx.draw(G, with_labels=True,node_size=500, node_color='#cdf7cb')
plt.margins(x=0.4)
plt.title(f"{title}")
plt.savefig(f'{title}.collocations.png', dpi=300)

plt.show()