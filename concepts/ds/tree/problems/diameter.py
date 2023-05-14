from prep.concepts.ds.tree.treebase import TreeBase

def diameter(r):
    if r:
        le = diameter(r.left)
        ri = diameter(r.right)
        global res
        res = max(res, 1+le+ri)
        return 1+ max(le, ri)
    return 0


res = float('-inf')
t1 = TreeBase()
for i in range(1, 8):
    t1.insert(i)

diameter(t1.root)
print(res)