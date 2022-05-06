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
            d.append([v, 0, u, v.label])
        else:
            if g.verify_edge(u, v.label):
                d.append([v, g.get_weight(u, v.label), u, v.label])
            else:
                d.append([v, math.inf, u, v.label])
    key = lambda a : a[1]
    d.sort(key=key)
    # loop
    while len(n) < len(g):
        # print(f"{len(n)} / {len(g)} -> {len(n) < len(g)}")
        # print(d)
        w = d.pop(0)
        w_label = w[0].label
        w_weight = w[1]
        w_prev = w[2]
        n.append(w_label)
        result.append((w_label, w_weight, w_prev))
        # print(f"{w_label}:")
        for v, weight in g.get_adjacents(w[0].label):
            # print(f"> {v.label}")
            v_label = v.label
            v_index = -1
            for i in range(len(d)):
                if d[i][0].label == v_label:
                    v_index = i
            # print(v_index)
            if v_label not in n:
                new_dv = w_weight + weight
                if new_dv < d[v_index][1]:
                    d[v_index][1] = new_dv
                    d[v_index][2] = w_label
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
