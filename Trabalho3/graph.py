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
            self._weight[len(self._weight)-1].append(0)

    # Adiciona uma aresta entre os vértices "a" e "b".
    def add_edge(self, a, b, w=None):
        if a != b:
            self._matrix[a][b] = 1
            self._matrix[b][a] = 1
            self._weight[a][b] = w
            self._weight[b][a] = w

    # Remove uma aresta entre os vértices "a" e "b".
    def remove_edge(self, a, b):
        if a != b:
            self._matrix[a][b] = 0
            self._matrix[b][a] = 0
            self._weight[a][b] = None
            self._weight[b][a] = None
    
    # Adiciona um peso em um vértice já existente.
    def set_weight(self, a, b, w):
        if a != b and self._matrix[a][b] == 1:
            self._weight[a][b] = w
            self._weight[b][a] = w
    
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

    # Encontra os vértices que podem ser alcançados a partir de um determinado vértice
    def reachable_vertices(self, v, reachable):
        current = self._matrix[v]
        reachable[v] = 1

        for i in range(len(current)):
            if current[i] == 1 and reachable[i] != 1:
                reachable = self.reachable_vertices(i, reachable)
        
        return reachable
    
    # Encontra quantos vértices podem ser alcançados a partir de um determinado vértice
    # Obs.: A contagem inclui o próprio vértice 'v'
    def count_reachable_vertices(self, v):
        var_reachable_vertices = self.reachable_vertices(v, [0]*len(self))
        count = sum(var_reachable_vertices)

        return count
    
    # Verifica se uma aresta é uma ponte
    def is_a_bridge(self, a, b):
        before = self.count_reachable_vertices(a)
        self.remove_edge(a, b)
        after = self.count_reachable_vertices(a)
        self.add_edge(a, b)

        return before > after

