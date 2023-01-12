class Graph:
    class Vertex:
        def __init__(self, ele):
            self.ele = ele

        def __hash__(self):
            return hash(id(self))

    class Edge:
        def __init__(self, u , v, ele=None):
            self.origin = u
            self.dest = v
            self.ele = ele

        def __hash__(self):
            return hash((self.origin, self.dest))

        def endpoint(self):
            return (self.origin, self.dest)

        def opposite(self, v):
            return self.dest if v is self.origin else self.origin

    def __init__(self, undirect = False):
        self.outgoing = {}
        self.incoming = {}
        if undirect:
            self.outgoing = self.incoming

    def is_direct(self):
        return self.outgoing is not self.incoming

    def insert_vertex(self, ele):
        v = self.Vertex(ele)
        self.outgoing[v] = {}
        if self.is_direct():
            self.incoming[v] = {}
        return v

    def insert_edge(self, u, v, ele=None):
        e = self.Edge(u, v, ele)
        self.outgoing[u][v] = e
        self.incoming[v][u] = e

    def incident(self, v, incoming=False):
        pl = self.incoming if incoming else self.outgoing
        for i in pl[v].values():
            yield i

    def edges(self):
        pl = set()
        ad = self.outgoing.values()
        for i in ad:
            pl.update(i.values())
            #print(i.values)
        # for i in ad.values():
        #     o = i.values()
        #     print(o)
        #     #pl.append()
        #     #print(pl)
        #print(pl)
        return pl

    def vertices(self):
        return self.outgoing.keys()

    def degree(self, v,  incoming=True):
        adj = self.incoming if incoming else self.outgoing
        return len(adj[v])

    def print_ed(self, v):
        l = []
        for i in v:
            l.append(i.origin.ele)
            l.append(i.dest.ele)
        return l
    def print(self):
        for i in self.outgoing:
            print(f'{i.ele}:  {self.print_ed(self.outgoing[i].values())}')
#
# ob = Graph()
#
# o1 = ob.insert_vertex(3)
# o2 = ob.insert_vertex(13)
# o3 = ob.insert_vertex(23)
# o4 = ob.insert_vertex(43)
# #o5 = ob.insert_vertex(33)
#
# ob.insert_edge(o1, o2)
# ob.insert_edge(o2, o3)
# ob.insert_edge(o1, o3)
# ob.insert_edge(o1, o4)
#

# for i in [o1,o2,o3,o4]:
#     for e in ob.incident(i):
#         print(f'{i.ele} =>  {e.origin.ele} -- {e.dest.ele}')

#
# 3 =>  3 13
# 3 =>  3 23
# 3 =>  3 43
# 13 =>  3 13
# 13 =>  13 23
# 23 =>  13 23
# 23 =>  3 23
# 43 =>  3 43