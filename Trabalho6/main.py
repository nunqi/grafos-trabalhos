from graph import Graph

import sys
import math


def dijkstra(g, u):
    n = [u]
    d = []
    for i in range(len(g)):
        if g.verify_edge(u, i) and i != u:
            d.append([g.get_weight(u, i), u])
        else:
            d.append([math.inf, u])
    while len(n) < len(g):
        w = -1
        min_aux = math.inf
        for i in range(len(d)):
            if d[i][0] <= min_aux and i not in n:
                w = i
                min_aux = d[i][0]
        n.append(w)
        for v in g.get_adjacents(w):
            v_name = v[0].name
            if v_name not in n:
                new_dv = d[w][0] + v[1]
                if new_dv < d[v_name][0]:
                    d[v_name][0] = new_dv
                    d[v_name][1] = w
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

g = Graph()
for i in range(int(file_info[0])):
    g.add_vertice(i)

for e in file_info[1]:
    g.add_edge(int(e[0])-1, int(e[1])-1, int(e[2]))


print(str(dijkstra(g, root)))
