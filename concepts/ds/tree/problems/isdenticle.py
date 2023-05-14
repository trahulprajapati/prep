from prep.concepts.ds.tree.treebase import TreeBase

def is_identicle(t1,t2):
    if t1 == None and t2 == None:
        return True

    if t1 != None and t2 != None:
        return t1.ele == t2.ele and is_identicle(t1.left, t2.left) and is_identicle(t1.right, t2.right)
    return False

t1 = TreeBase()
t2 = TreeBase()
for i in range(1, 8):
    t1.insert(i)

for i in range(1, 8):
    t2.insert(i)


print(is_identicle(t1.root, t2.root))
