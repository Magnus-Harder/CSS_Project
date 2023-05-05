import random
import networkx as nx
from community.community_louvain import modularity
from tqdm import tqdm

def double_edge_swap(G, n_swap=100):
    G_swapped = G.copy()
    for swap in range(n_swap):
        # Get random edge
        edge1,edge2 = random.sample(list(G_swapped.edges),2)

        u,v = edge1
        x,y = edge2

        # Check swap is valid
        if u == y or v == x: 
            continue

        # Check if new edges already exist
        if G_swapped.has_edge(u,y) or G_swapped.has_edge(v,x):
            continue

        # Remove edge
        G_swapped.remove_edge(u,v)
        G_swapped.remove_edge(x,y)

        # Add new edges
        G_swapped.add_edge(u,y)
        G_swapped.add_edge(x,v)

    return G_swapped
# Define function for randomized version of double edge swap modularity

def ex_modularity(G,partition,n_swap=100, experiments=1000):

    modularity_values = []

    for experiment in tqdm(range(experiments)):
        G_swapped = double_edge_swap(G, n_swap=n_swap)
        modularity_values.append(modularity(partition, G_swapped))

    return modularity_values

