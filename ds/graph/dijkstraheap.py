from prep.ds.graph.graphbase import Graph
from prep.ds.heap.heapbase import HeapBase

def dijkstra(g, s):
    d = {}
    loc = {}
    h = HeapBase()

    for v in g.vertices():
        if v is s:
            d[v] = 0
        else:
            d[v] = float('inf')
        loc[v] = h.add(d[v], v)

    #shortest path
    out = {}
    while not h.is_empty():
        k, u = h.remove_min()
        #out[u.ele] = k
        out[u] = k
        del loc[u]
        for e in g.incident(u):
            v = e.opposite(u)
            if v not in out:
                #relaxation
                ew = d[u] + e.ele
                if ew < d[v]:
                    d[v] = ew
                    h.update(loc[v], ew, v)
    return out

# reconstruct path to v from s , d is destance of v
def reconstruct_shortedpath(g, s, d):
    tree = {}
    for v in d:
        if v is not s:
            for e in g.incident(v, True):
                u = e.opposite(v)
                if e.ele + d[u] == d[v]:
                    tree[v] = e
    return tree

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

pl = dijkstra(ob, v1)
#print(pl)
for i in pl:
    print(i.ele, pl[i])

print('recontrsut')
tr = reconstruct_shortedpath(ob, v1, pl)
# #print(tr)
# for i in tr:
#     print(i.ele, tr[i].ele)

# for i in tr:
#     print(i.ele, f'{tr[i].origin.ele, tr[i].dest.ele}')