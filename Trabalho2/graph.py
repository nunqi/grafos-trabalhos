class Graph:

    def __init__(self, n=0):
        self._matrix = []
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

    # Adiciona um vértice no grafo.
    def add_vertice(self):
        for v in self._matrix:
            v.append(0)
        self._matrix.append([])
        for i in range(len(self._matrix)):
            self._matrix[len(self._matrix)-1].append(0)

    # Adiciona uma aresta entre os vértices "a" e "b".
    def add_edge(self, a, b):
        if a != b:
            self._matrix[a][b] = 1
            self._matrix[b][a] = 1
    
    # Retorna a densidade de um vértice específico.
    def vertice_density(self, vertice):
        if isinstance(vertice, int):
            return sum(self._matrix[vertice])
        elif isinstance(vertice, list):
            return sum(vertice)

    # Verifica se existe uma aresta entre os pontos "a" e "b".
    def verify_edge(self, a, b):
        return self._matrix[a][b] == 1
