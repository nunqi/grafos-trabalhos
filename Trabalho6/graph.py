class Node:
    def __init__(self, name):
        self.name = name
        self.adjacents = []
    
    def __str__(self):
        return str(self.name)

    def add_edge_to(self, v, weight):
        self.adjacents.append((v, weight))

class Graph:
    def __init__(self):
        self.vertices = []

    def __str__(self):
        string = ""
        for v in self.vertices:
            string += str(v.name) + ": ["
            for a in v.adjacents:
                string += str(a) + ", "
            string = string.removesuffix(", ")
            string += "]\n"
        return string
    
    def __len__(self):
        return len(self.vertices)
    
    def __iter__(self):
        return iter(self.vertices)
    
    def __getitem__(self, n):
        return self.vertices[n]

    def add_vertice(self, name):
        self.vertices.append(Node(name))

    def get_vertice_pointer(self, v):
        for vertice in self.vertices:
            if vertice.name == v:
                return vertice

    def add_edge(self, a, b, weight):
        v_from = self.get_vertice_pointer(a)
        v_to = self.get_vertice_pointer(b)
        v_from.add_edge_to(v_to, weight)

    def verify_edge(self, a, b):
        index = 0
        for i in range(len(self.vertices)):
            if self.vertices[i].name == a:
                index = i
                break
        for a in self.vertices[index].adjacents:
            if a[0].name == b:
                return True
        return False

    def get_adjacents(self, v):
        # talvez seja uma boa mudar para retornar um cópia
        return self.get_vertice_pointer(v).adjacents
    
    def get_weight(self, v, w):
        for a in self.get_vertice_pointer(v).adjacents:
            if a[0].name == w:
                return a[1]
        return None