from graph import Graph

import math
import copy
import networkx as nx
import matplotlib.pyplot as plt


def bellman_ford(graph, u):
    # setup
    g = copy.deepcopy(graph)
    g.get_vertice_reference(u).distance = 0
    edges = []
    for v in g:
        for w, weight in v.adjacents:
            edges.append((v.label, w.label))
    # loop
    for i in range(len(g)-1):
        for e in edges:
            g.relax(e[0], e[1])
    # result
    result = []
    for v in g:
        result.append((v.label, v.distance, v.prev))
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
                break
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


for v in g:
    print(f" {v.label} -----------")
    bf = bellman_ford(g, v.label)
    print(f"Bellman-Ford: {bf}")
    for a in g:
        print(f"{a.label}: {distance(bf, a.label)} / {path(bf, v.label, a.label)}")
    # visualize(bf)
