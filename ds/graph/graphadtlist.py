class Graph:
    class Vertex:
        def __init__(self, ele):
            self.ele = ele

    class Edge:
        def __hash__(self,ele=None):
            self.ele = ele
            self.origin = None
            self.dest = None

        def endpoint(self):
            return (self.origin, self.dest)

    def __init__(self, directed = False):
        self.outgoing = []
        self.incoming = []
        if directed:
            self.outgoing = self.incoming

    def is_direct(self):
        return self.outgoing is not self.incoming

    def insert_vertex(self, ele):
        v = self.Vertex(ele)
        self.outgoing.append(v)

        if self.is_direct():
            self.incoming = self.incoming

