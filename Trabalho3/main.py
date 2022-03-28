from graph import Graph
import json
import sys


def is_euler(g):
    odd_vertices = 0

    for v in g:
        degree = g.vertice_density(v)
        if degree % 2 != 0:
            odd_vertices += 1
    
    if odd_vertices == 0:
        return "Euleriano"

    if odd_vertices == 2:
        return "Semi-euleriano"
    
    if odd_vertices > 2:
        return "Não euleriano"

    return "Error: Entrada inválida"

def fleury(graph):
    g = graph   # Cópia do grafo

    # Escolher o vértice inicial
    v = 0   # Vértice inicial
    for i in range(len(g)):
        if g.vertice_density(i) % 2 != 0:
            v = i
            break
    
    # Começar o algoritmo


try:
    graph_id = sys.argv[1]
except:
    graph_id = input("Grafo que será usado: ")

data = json.load(open('data.json'))
data_graph = data["graph" + graph_id]   

g = Graph(data_graph['vertices'])

for e in data_graph['edges']:
    g.add_edge(e[0], e[1])


print(str(fleury(g)))

