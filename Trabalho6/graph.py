class Graph:

    def __init__(self, n=0):
        self._matrix = []
        self._weight = []
        for i in range(n):
            self.add_vertice()

    def __str__(self):
        string = ""
        for v in self._matrix:
            string += str(v)
            string += "\n"
        return string

    def __iter__(self):
        return iter(self._matrix)

    def __len__(self):
        return len(self._matrix)
    
    def __getitem__(self, n):
        return self._matrix[n]

    # Adiciona um vértice no grafo.
    def add_vertice(self):
        for v in self._matrix:
            v.append(0)
        self._matrix.append([])
        for i in range(len(self._matrix)):
            self._matrix[len(self._matrix)-1].append(0)

        for v in self._weight:
            v.append(None)
        self._weight.append([])
        for i in range(len(self._weight)):
            self._weight[len(self._weight)-1].append(None)

    # Adiciona uma aresta entre os vértices "a" e "b".
    def add_edge(self, a, b, w):
        if a != b:
            self._matrix[a][b] = 1
            self._weight[a][b] = w

    # Remove uma aresta entre os vértices "a" e "b".
    def remove_edge(self, a, b):
        if a != b:
            self._matrix[a][b] = 0
            self._weight[a][b] = None
    
    # Adiciona um peso em um vértice já existente.
    def set_weight(self, a, b, w):
        if a != b and self._matrix[a][b] == 1:
            self._weight[a][b] = w
    
    # Retorna o peso de um vértice específico.
    def get_weight(self, a, b):
        return self._weight[a][b]
    
    # Retorna a densidade de um vértice específico.
    def vertice_density(self, vertice):
        if isinstance(vertice, int):
            return sum(self._matrix[vertice])
        elif isinstance(vertice, list):
            return sum(vertice)

    # Verifica se existe uma aresta entre os pontos "a" e "b".
    def verify_edge(self, a, b):
        return self._matrix[a][b] == 1

    def get_adjacents(self, v):
        result = []
        vertice = self._matrix[v]

        for i in range(len(vertice)):
            if vertice[i] == 1:
                result.append(i)

        return result

    def find_min(self, v):
        result = -1
        for j in range(len(self._matrix[v])):
            if self.verify_edge(v, j):
                result = j
        for i in range(len(self._matrix[v])):
            if self.verify_edge(v, i) and self.get_weight(v, i) <= self.get_weight(v, result):
                result = i
        return result
