class Graph:
    def __init__(self, v):
        self.graph = [[0 for j in range(v)] for i in range(v)]

g = Graph(3)
print(g.graph)