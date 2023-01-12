#from prep.ds.graph.graphbase import Graph
from prep.concepts.ds.graph.graphbase import Graph
from prep.concepts.ds.heap.heapbase import HeapBase

class Partition(object):
    class Node:
        def __init__(self, ele):
            self.ele = ele
            self.parent = self
            self.size = 0

    def make_group(self, ele):
        return self.Node(ele)

    def find(self, p):
        if p.parent != p:
            p.parent = self.find(p.parent)
        return p.parent

    def union(self, p, q):
        a = self.find(p)
        b = self.find(q)

        if a != b:
            if a.size < b.size:
                b.parent = a
                a.size += b.size
            else:
                a.parent = b
                b.size += a.size


def kuskals(g):
    #make group of all v
    loc = {}
    p = Partition()
    pq = HeapBase()
    size = 0
    for v in g.vertices():
        size += 1
        #print(v)
        loc[v] = p.make_group(v)

    #add all edge to heap
    for e in g.edges():
        pq.add(e.ele, e)

    #iter
    tree = []
    n = 0
    while len(tree) != size-1 and not pq.is_empty():
        w, e = pq.remove_min()
        u, v = e.endpoint()
        fi = p.find(loc[u])
        se = p.find(loc[v])

        if fi != se:
            p.union(fi, se)
            n += e.ele
            tree.append(e)
    print(n)
    return tree

#output
#('a', 'b') ('b', 'c') ('b', 'd') ('c', 'e') ('d', 'f')

ob = Graph()

v1 = ob.insert_vertex('a')
v2 = ob.insert_vertex('b')
v3 = ob.insert_vertex('c')
v4 = ob.insert_vertex('d')
v5 = ob.insert_vertex('e')
v6 = ob.insert_vertex('f')

ob.insert_edge(v1, v2, 2)
ob.insert_edge(v1, v3, 4)
ob.insert_edge(v2, v3, 1)
ob.insert_edge(v2, v4, 2)
ob.insert_edge(v3, v5, 3)
ob.insert_edge(v4, v6, 1)
ob.insert_edge(v5, v6, 5)
ob.insert_edge(v5, v4, 2)

pl = kuskals(ob)
#print(pl, n)
#print(pl)
for i in pl:
    print((i.origin.ele, i.dest.ele))

# /usr/local/bin/python3.7 /Users/rahul.prajapati/rahul/prep/ws1/prep/ds/graph/mstprimsalgo.py
# ('a', 'b')
# ('b', 'c')
# ('b', 'd')
# ('c', 'e')
# ('d', 'f')

#
# ('a', 'b')
# ('b', 'c')
# ('b', 'd')
# ('c', 'e')
# ('d', 'f')

# ('b', 'c')
# ('d', 'f')
# ('a', 'b')
# ('e', 'd')
# ('b', 'd')
#
