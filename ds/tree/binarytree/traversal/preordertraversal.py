from prep.ds.tree.treebase import TreeBase

class PrerderTreversal(TreeBase):
    def __init__(self):
        super().__init__()

    #recursive
    def recursive_tranversal(self, p):
        if p:
            print(p.ele, end=' ')
            self.recursive_tranversal(p.left)
            self.recursive_tranversal(p.right)

    def stack_traversal(self, p):
        stk = [p]
        while len(stk) != 0:
            el = stk.pop()
            print(el.ele, end= ' ')
            if el.right:
                stk.append(el.right)
            if el.left:
                stk.append(el.left)

    def morris_traversal(self, root):
        pass

t = PrerderTreversal()

for i in range(10):
    t.insert(i)

print('Method 1: Recursive')
t.recursive_tranversal(t.root)

print('Method 1: Stack')
t.stack_traversal(t.root)