from prep.ds.tree.treebase import TreeBase

class PostorderTreversal(TreeBase):
    def __init__(self):
        super().__init__()

    def recursive_tranvewrsal(self,p):
        if p:
            self.recursive_tranvewrsal(p.left)
            self.recursive_tranvewrsal(p.right)
            print(p.ele, end=' ')

    def stack_traversal(self, p):
        stk = [[p, 0]]
        while len(stk) != 0:
            el, st = stk.pop()
            if el != None:
                if st:
                    print(el.ele, end=' ')
                    #stk.pop()
                else:
                    stk.append([el, 1])
                    stk.append([el.right, 0])
                    stk.append([el.left, 0])




t = PostorderTreversal()

for i in range(1, 8):
    t.insert(i)

print('Method 1: Recursive')
t.recursive_tranvewrsal(t.root)

print('Method 1: Recursive')
t.stack_traversal(t.root)