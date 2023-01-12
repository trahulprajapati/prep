from prep.concepts.ds.graph.graphbase import Graph
from prep.concepts.ds.heap.heapbase import HeapBase

def primsalgo(g):
    loc = {}
    tree = []
    pq = HeapBase()
    d = {}

    n = 0
    for v in g.vertices():
        if len(d) == 0:
            d[v] = 0
        else:
            d[v] = float('inf')
        loc[v] = pq.add(d[v], (v, None))

    while not pq.is_empty():
        ele, val = pq.remove_min()
        u, e = val
        del loc[u]
        if e is not None:
            n += e.ele
            tree.append(e)
        for ed in g.incident(u):
            v = ed.opposite(u)
            if v not in tree:
                if ed.ele < d[v]:
                    d[v] = ed.ele
                    pq.update(loc[v], d[v], (v, ed))
    print(n)
    return tree

#input
#     B       D
# A                F
#     C       E
#
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

pl = primsalgo(ob)
#print(pl, n)
#print(pl)
for i in pl:
    print((i.origin.ele, i.dest.ele))
