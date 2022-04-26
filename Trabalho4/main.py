from graph import Graph
from tree import Tree
from queue import Queue

import sys
import networkx as nx
import matplotlib.pyplot as plt


def bfs(g, root):
    q = Queue(len(g))
    aux = Graph(len(g))
    tree = Tree(root)

    q.put(root)
    explored = [root]
    while not q.empty():
        v = q.get()
        for w in g.get_adjacents(v):
            if w not in explored:
                explored.append(w)
                q.put(w)
                tree.add(w, v)
                # aux.add_edge(w, v)
    # q.put(root)
    # explored = [root]
    # while not q.empty():
    #    v = q.get()
    #    for w in aux.get_adjacents(v):
    #        if w not in explored:
    #            explored.append(w)
    #            q.put(w)
    #            tree.add(w, v)

    return tree


def find_distance(tree, v):
    return tree.distance(v)


def find_path(tree, v):
    return tree.path(v)


def visualize(tree):
    edges = tree.get_all_edges()
    #print(str(edges))
    g = nx.Graph()
    g.add_edges_from(edges)
    nx.draw_networkx(g)
    plt.show()


def print_connections(g):
    for i in range(len(g)):
        a = g.get_adjacents(i)
        b = []
        for j in a:
            b.append(j+1)
        print(str(i+1) + ": " + str(b))


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
    root = int(sys.argv[1])
    i = int(sys.argv[2])
except:
    root = int(input("Raiz: "))
    i = int(input("Vértice que será testado: "))


file_info = get_file()

g = Graph(int(file_info[0]))

for e in file_info[1]:
    g.add_edge(int(e[0]), int(e[1]))


tree = bfs(g, root)
print("Distância: " + str(find_distance(tree, i)))
print("Caminho: " + str(find_path(tree, i)))
visualize(tree)

