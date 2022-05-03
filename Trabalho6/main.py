from graph import Graph
from tree import Tree

import sys
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(g):
    pass


def visualize(tree):
    edges = tree.get_all_edges()
    for e in edges:
        e[0] += 1
        e[1] += 1
    # print(str(edges))
    g = nx.Graph()
    g.add_edges_from(edges)
    nx.draw_networkx(g)
    plt.show()


def get_file(filename="content.txt"):
    vertices = []

    with open(filename) as graph_file:
        for line in graph_file:
            try:
                if not len(line.split()) > 1:
                    edges = line
                else:
                    vertices.append(line.split())
            except:
                print("Grafo nao esta nos padraes de execucao.")

    return edges, vertices


try:
    root = int(sys.argv[1]) - 1
    # i = int(sys.argv[2]) - 1
except:
    root = int(input("Raiz: ")) - 1
    # i = int(input("Vértice que será testado: ")) - 1


file_info = get_file()

g = Graph(int(file_info[0]))

for e in file_info[1]:
    g.add_edge(int(e[0])-1, int(e[1])-1)


# tree = dfs(g, root)
tree = recursive_dfs(g, root)
visualize(tree)
