from prep.concepts.ds.tree.treebase import TreeBase
# from prep.concepts.ds.tree.treebase import TreeBase
# t1 = TreeBase()
# for i in range(1, 8):
#     t1.insert(i)

def get_hieght(r):
    if r:
        return 1+ max(get_hieght(r.left), get_hieght(r.right))
    return 0

t1 = TreeBase()
for i in range(1, 8):
    t1.insert(i)


print(get_hieght(t1.root))