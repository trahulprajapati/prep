from prep.concepts.ds.graph.graphbase import Graph


def DFStraversal(g, u, desc):
    for e in g.incident(u):
        v = e.opposite(u)
        #print(e.origin.ele, e.dest.ele, v.ele, u.ele)
        if v not in desc:
            desc[v] = e
            DFStraversal(g, v, desc)

def BFStravenrsal(g, s, desc):
    lvl = [s]
    while len(lvl) > 0:
        nxtl = []
        for u in lvl:
            for e in g.incident(u):
                v = e.opposite(u)
                if v not in desc:
                    desc[v] = e
                    nxtl.append(v)
        lvl = nxtl

def reconstruct(u, v, desc):
    li = []

    if v in desc:
        wk = v
        while wk is not u:
            e = desc[wk]
            par= e.opposite(wk)
            li.append(par)
            wk = par
    li.reverse()
    return li
ob = Graph()

o1 = ob.insert_vertex(3)
o2 = ob.insert_vertex(13)
o3 = ob.insert_vertex(23)
o4 = ob.insert_vertex(43)
#o5 = ob.insert_vertex(33)

ob.insert_edge(o1, o2)
ob.insert_edge(o2, o3)
ob.insert_edge(o3, o1)
ob.insert_edge(o1, o4)

print('=======')
h = {o1:None}
for i in [o1,o2,o3,o4]:
    for e in ob.incident(i):
        print(f'{i.ele} =>  {e.origin.ele} -- {e.dest.ele}')
DFStraversal(ob, o1, h)
for i in h:
    p = h[i]
    if p:
        print(f'{i.ele} =>  {p.origin.ele} -- {p.dest.ele}')

h= {}
BFStravenrsal(ob, o1, h)

print('=======',len(h))
for i in h:
    p = h[i]
    if p:
        print(f'{i.ele} =>  {p.origin.ele} -- {p.dest.ele}')

# li = reconstruct(o1, o3, h)
# for i in li:
#    print(i.ele)
#print(li)