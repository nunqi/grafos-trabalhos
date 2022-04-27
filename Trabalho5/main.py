from graph import Graph
from tree import Tree

import sys
import networkx as nx
import matplotlib.pyplot as plt


def dfs(g, root):
    q = []  # stack
    tree = Tree(root)

    q.append(root)
    explored = []
    previous_v = root
    while q:
        input()
        v = q.pop()
        print("r: " + str(v))
        print(str(q))
        if v not in explored:
            if previous_v != v:
                if (not g.verify_edge(previous_v, v)) or (previous_v in explored):
                    for i in range(len(explored)-1, -1, -1):
                        u = explored[i]
                        if g.verify_edge(u, v):
                            previous_v = u
                            print("New previous_v: " + str(previous_v))
                            break
                tree.add(v, previous_v)
                print("Added " + str(v) + " to " + str(previous_v))
            explored.append(v)
            for w in g.get_adjacents(v):
                q.append(w)
                print("a: " + str(w))
                print(str(q))
        previous_v = v

    # tree.show()

    return tree


def recursive_dfs(g, root):
    explored = []
    tree = Tree(root)
    rdfs(root, root, g, explored, tree)
    return tree


def rdfs(u, previous_u, g, explored, tree):
    if previous_u != u:
        tree.add(u, previous_u)
    explored.append(u)
    for v in g.get_adjacents(u):
        if v not in explored:
            rdfs(v, u, g, explored, tree)


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
