from graph import Graph

import sys
import math


def dijkstra(g, u):
    n = [u]
    d = []
    for i in range(len(g)):
        if i == u:
            d.append(0)
        else:
            if g.verify_edge(u, i):
                d.append(g.get_weight(u, i))
            else:
                d.append(math.inf)
    while len(n) < len(g):
        w = g.find_min(u)
        for v in g.get_adjacents(w):
            if w not in n:
                n.append(w)
                d[v] = min(d[v], d[w] + g.get_weight(w, v))
    return d


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
    g.add_edge(int(e[0])-1, int(e[1])-1, int(e[2]))


print(str(dijkstra(g, root)))
