class Graph:
    class Vertex:
        def __init__(self, ele):
            self.ele = ele

        def __hash__(self):
            return hash(id(self))

    class Edge:
        def __init__(self,u , v, ele=None):
            self.ele = ele
            self.origin = u
            self.dest = v

        def endpoint(self):
            return (self.origin, self.dest)

        def opposite(self, v):
            return self.origin if v is self.origin else self.dest

        def __hash__(self):
            return hash((self.origin, self.dest))

    def __init__(self, is_directed = False):
        self.outgoing = {}
        self.incoming = {}

        if not is_directed:
            self.incoming = self.outgoing

    def is_direct(self):
        return self.incoming is not self.outgoing

    def insert_vertex(self, ele):
        v = self.Vertex(ele)
        self.outgoing[v] = {}
        if self.is_direct():
            self.incoming[v] = {}

        return v

    def insert_edge(self, u, v, ele=None):
        e = self.Edge(u , v, ele)
        self.outgoing[u][v] = e
        self.incoming[v][u] = e

    def get_edge(self, u, v):
        return self.outgoing[u].get(v)

    def all_vertex(self):
        return self.outgoing.keys()

    def all_edges(self):
        e = self.outgoing.values()
        for i in e:
            print(i.values())


    def incident(self, v, incoming=False):
        #p = self.outgoing.get(v)
        pl = self.outgoing
        if incoming:
            pl = self.incoming
        for i in pl[v].values():
            #print(i) # return obj
            yield i

    def verted_count(self):
        return len(self.outgoing)

    def edge_count(self):
        n = 0
        for i in self.outgoing.values():
            n += len(i)
        if self.is_direct():
            return n
        else:
            return n // 2

    def degree(self, v):
        v = self.outgoing[v]
        return len(v)

    #     1
    #
    # 3       4       5

