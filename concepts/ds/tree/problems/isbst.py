from prep.concepts.ds.tree.treebase import TreeBase

#method1
def is_bst1(p, mi, ma):
    if p == None:
        return True
    if p.ele < mi or p.ele > ma:
        return False
    return is_bst1(p.left, mi, p.ele-1) and is_bst1(p.right, p.ele+1, ma)


def is_bst2(r):
    prev = None
    while r != None:
        if r.left == None:
            if prev != None and prev.ele >= r.ele:
                return False
            prev = r
            r = r.right
        else:
            rm = r.left
            while rm.right != None and rm.right != r:
                rm = rm.right
            if rm.right == None:
                rm.right = r
                r = r.left
            else:
                rm.right = None
                if prev != None and prev.ele >= r.ele:
                    return False
                prev = r
                r= r.right
    return True
t1 = TreeBase()
for i in range(1, 8):
    t1.insert(i)

print(is_bst1(t1.root, float('-inf'), float('inf')))

print(is_bst2(t1.root))