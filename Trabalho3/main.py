from graph import Graph
import json
import sys
import copy


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

    if is_euler(graph) != "Euleriano" and is_euler(graph) != "Semi-euleriano":
        return []

    g = copy.deepcopy(graph)   # Cópia do grafo

    # Escolher o vértice inicial
    current_v = 0   # Vértice inicial
    for i in range(len(g)):
        if g.vertice_density(i) % 2 != 0:
            current_v = i
            break
    
    # Começar o algoritmo
    path = [current_v]
    flag = True
    while flag:
        flag = False
        for next_v in range(len(g[current_v])):
            if g[current_v][next_v] == 1 and not g.is_a_bridge(current_v, next_v):
                g.remove_edge(current_v, next_v)
                current_v = next_v
                flag = True
                break
        path.append(current_v)
    path.pop()
    
    return path

def fleury_sum(path):
    count = 0
    for i in range(len(path)):
        try:
            w = g.get_weight(path[i], path[i+1])
            if w != None:
                count += w
        except:
            pass
    
    return count


try:
    graph_id = sys.argv[1]
except:
    graph_id = input("Grafo que será usado: ")

data = json.load(open('data.json'))
data_graph = data["graph" + graph_id]   

g = Graph(data_graph['vertices'])

for e in data_graph['edges']:
    g.add_edge(e[0], e[1], 1)

print("Tipo: " + is_euler(g))
print("Caminho: " + str(fleury(g)))
print("Soma: " + str(fleury_sum(fleury(g))))


