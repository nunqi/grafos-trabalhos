from graph import Graph

import sys
import math


def dijkstra(g, u):
    # setup
    n = []
    result = []
    d = []
    for v in g:
        if v.label == u:
            d.append([v, 0, u])
        else:
            d.append([v, math.inf, u])
    key = lambda a : a[1]
    d.sort(key=key)
    # loop
    while len(n) < len(g):
        w = d.pop(0)
        n.append(w[0].label)
        result.append((w[0].label, w[1], w[2]))
        for v, weight in g.get_adjacents(w[0].label):
            if v.label not in n:
                v_index = -1
                for i in range(len(d)):
                    if d[i][0].label == v.label:
                        v_index = i
                new_dv = w[1] + weight
                if new_dv < d[v_index][1]:
                    d[v_index][1] = new_dv
                    d[v_index][2] = w[0].label
                    d.sort(key=key)
    result.sort(key=key)
    return result


def get_file(filename="content.txt"):
    vertices = []

    with open(filename) as graph_file:
        for line in graph_file:
            try:
                vertices.append(line.split())
            except:
                print("Grafo nao esta nos padraes de execucao.")

    return vertices


# init graph
g = Graph()
for e in get_file():
    g.add_edge(e[0], e[1], int(e[2]))


print(str(dijkstra(g, 'a')))
