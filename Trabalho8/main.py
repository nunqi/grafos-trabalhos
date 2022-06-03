import math


def floyd_warshall(matrix):
    d = matrix
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                aux = d[i][k] + d[k][j]
                if aux < d[i][j]:
                    d[i][j] = aux
    return d


def print_matrix(m):
    for v in m:
        print(str(v))


def read_matrix_file(filename="content.txt"):
    with open(filename) as graph_file:
        matrix = []
        for line in graph_file:
            v = []
            try:
                line_v = line.split()
                for s in line_v:
                    if s == "i":
                        v.append(math.inf)
                    else:
                        v.append(int(s))
                matrix.append(v)
            except:
                print("Grafo nao esta nos padraes de execucao.")

    return matrix


matrix = read_matrix_file()
for line in floyd_warshall(matrix):
    print(str(line))
