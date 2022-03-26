from graph import Graph
import json
import sys


def dirac(g):
    if len(g) < 3:
        return False
    
    for v in g:
        if g.vertice_density(v) < len(g)/2:
            return False
    
    return True

def ore(g):
    for i in range(len(g)):
        for j in range(len(g)):
            if i != j and g.vertice_density(i) + g.vertice_density(j) < len(g):
                return False
    return True


def bondy(g):
    flag = True

    while flag:
        flag = False
        for i in range(len(g)):
            for j in range(len(g)):
                if i != j and (not g.verify_edge(i, j)) and g.vertice_density(i) + g.vertice_density(j) >= len(g):
                    g.add_edge(i, j)
                    flag = True

    # print(g)
    for v in g:
        if g.vertice_density(v) != len(g)-1:
            return False
    return True

def run(g):
    print(g)
    print("Dirac: " + str(dirac(g)))
    print("Ore: " + str(ore(g)))
    print("Bondy & Chvátal: " + str(bondy(g)))

try:
    graph_id = sys.argv[1]
except:
    graph_id = input("Grafo que será usado: ")

data = json.load(open('data.json'))
data_graph = data["graph" + graph_id]   

g = Graph(data_graph['vertices'])

for e in data_graph['edges']:
    g.add_edge(e[0], e[1])

run(g)
