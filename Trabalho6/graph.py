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
    def add_edge(self, a, b, w=None):
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
    
    # Encontra quantos vértices podem ser alcançados a partir de um determinado vértice
    def count_reachable_vertices(self, v):
        return self.crv(v, [0]*len(self))
    def crv(self, v, reachable, count=0):
        current = self._matrix[v]
        reachable[v] = 1

        for i in range(len(current)):
            if current[i] == 1 and reachable[i] != 1:
                count += 1
                self.crv(i, reachable, count)

        return count
    
    # Verifica se uma aresta é uma ponte
    def is_a_bridge(self, a, b):
        if self.vertice_density(a) == 1:
            return False
        if self.vertice_density(b) == 1:
            return True
        
        weight = self.get_weight(a, b)
        before = self.count_reachable_vertices(a)
        self.remove_edge(a, b)
        after = self.count_reachable_vertices(a)
        self.add_edge(a, b, weight)

        return before > after

