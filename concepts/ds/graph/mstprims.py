from prep.concepts.ds.graph.graphbase import Graph
from prep.concepts.ds.heap.heapbase import HeapBase

def prims(g):
    d = {}
    loc = {}
    h = HeapBase()

    #find distance
    for v in g.vertices():
        if len(d) == 0:
            d[v] = 0
        else:
            d[v] = float('inf')
        loc[v] = h.add(d[v], (v, None))

    #create tree
    tree = []
    n = 0

    while not h.is_empty():
        k, val = h.remove_min()
        #print(k, val)
        u, ed = val
        del loc[u]

        if ed is not None:
            tree.append(ed)
            n += k
        for e in g.incident(u):
            v = e.opposite(u)
            if v not in tree:
                if e.ele < d[v]:
                    d[v] = e.ele
                    h.update(loc[v], d[v], (v, e))
    return (tree, n)
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

pl, n = prims(ob)
#print(pl, n)
#print(pl)
for i in pl:
    print((i.origin.ele, i.dest.ele))

