import math


class Node:
    def __init__(self, label):
        self.label = label
        self.adjacents = []
        self.distance = math.inf
        self.prev = None

    def __str__(self):
        return str(self.label)

    def add_edge_to(self, v, weight):
        self.adjacents.append((v, weight))


class Graph:
    def __init__(self):
        self.vertices = []

    def __str__(self):
        string = ""
        for v in self.vertices:
            string += str(v.label) + ": ["
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

    def add_vertice(self, label):
        self.vertices.append(Node(label))

    def get_vertice_reference(self, v):
        for vertice in self.vertices:
            if vertice.label == v:
                return vertice

    def add_edge(self, a, b, weight):
        v_from = self.get_vertice_reference(a)
        if v_from is None:
            self.add_vertice(a)
            v_from = self.get_vertice_reference(a)
        v_to = self.get_vertice_reference(b)
        if v_to is None:
            self.add_vertice(b)
            v_to = self.get_vertice_reference(b)
        v_from.add_edge_to(v_to, weight)

    def verify_edge(self, a, b):
        a_pointer = self.get_vertice_reference(a)
        for v, w in a_pointer.adjacents:
            if v.label == b:
                return True
        return False

    def get_adjacents(self, v):
        return self.get_vertice_reference(v).adjacents

    def get_weight(self, v, w):
        for a in self.get_vertice_reference(v).adjacents:
            if a[0].label == w:
                return a[1]
        return None

    def relax(self, e1, e2):
        w = self.get_vertice_reference(e1)
        v = self.get_vertice_reference(e2)
        d = w.distance + self.get_weight(e1, e2)
        if v.distance > d:
            v.distance = d
            v.prev = e1
