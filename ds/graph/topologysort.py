from prep.ds.graph.graphbase import Graph

def topolocal_srt(g):
    topo = []
    ready = []
    incount = {}

    #calcuate the degree
    for u in g.vertices():
        deg = g.degree(u)
        incount[u] = deg
        if deg == 0:
            ready.append(u)
    # create topo
    while len(ready) > 0:
        u = ready.pop()
        topo.append(u)
        for e in g.incident(u):
            v = e.opposite(u)
            incount[v] -= 1
            if incount[v] == 0:
                ready.append(v)
    return topo

ob = Graph()

o1 = ob.insert_vertex(3)
o2 = ob.insert_vertex(13)
o3 = ob.insert_vertex(23)
o4 = ob.insert_vertex(43)
o5 = ob.insert_vertex(33)

ob.insert_edge(o1, o2)
ob.insert_edge(o2, o3)
ob.insert_edge(o3, o4)
ob.insert_edge(o4, o5)

pl = topolocal_srt(ob)
for i in pl:
    print(i.ele)
print(pl)