from graph import Graph

import math
import networkx as nx
import matplotlib.pyplot as plt


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
    d.sort(key=lambda a: a[1])
    # loop
    while len(n) < len(g):
        w = d.pop(0)
        n.append(w[0].label)
        result.append([w[0].label, w[1], w[2]])
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
                    d.sort(key=lambda a: a[1])
    result.sort(key=lambda a: a[1])
    for t in result:
        if t[1] == math.inf:
            t[2] = None
    return result


def distance(arr, goal):
    for a in arr:
        if a[0] == goal:
            return a[1]
    return -1


def path(arr, origin, goal):
    result = [goal]
    next_v = goal
    while next_v != origin:
        for a in arr:
            if a[0] == next_v:
                result.append(a[2])
                next_v = a[2]
        if next_v is None:
            return []
    return result


def visualize(arr):
    edges = []
    for a in arr:
        if a[0] != a[2] and a[1] != math.inf:
            edges.append([a[0], a[2]])
    g = nx.Graph()
    g.add_edges_from(edges)
    nx.draw_networkx(g)
    plt.show()


def get_file(filename="contentt.txt"):
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


for v in g:
    print(f" {v.label} -----------")
    dij = dijkstra(g, v.label)
    print(f"Dijkstra: {dij}")
    for a in g:
        print(f"{a.label}: {distance(dij, a.label)} / {path(dij, v.label, a.label)}")
    visualize(dij)
