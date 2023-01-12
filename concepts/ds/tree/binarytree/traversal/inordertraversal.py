from prep.concepts.ds.tree.treebase import TreeBase

class InorderTreversal(TreeBase):
    def __init__(self):
        super().__init__()

    #time: O(n^2), spcace: O(h)
    def recurring_tranversal(self, p):
        if p:
            self.recurring_tranversal(p.left)
            print(p.ele, end=' ')
            self.recurring_tranversal(p.right)

    #stack
    #time: O(n), space O(h)
    def stack_traversal(self, p):
        stk = []
        while (p != None or len(stk) != 0):
            if p != None:
                stk.append(p)
                p = p.left
            else:
                el = stk.pop()
                print(el.ele, end=' ')
                p = el.right


    #morris Time: O(n)
    def morris_inorder(self, p):
        wk = p
        while wk != None:
            if wk.left == None:
                print(wk.ele, end=' ')
                wk = wk.right
            else:
                rightmost = wk.left
                while rightmost.right != None and rightmost.right != wk:
                    rightmost = rightmost.right
                if rightmost.right == None:
                    rightmost.right = wk
                    wk = wk.left
                else:
                    rightmost.right = None
                    print(wk.ele, end=' ')
                    wk = wk.right
                    #ri

    #sucessor
    # time: O(h), space O(h)
    # parent is not available so
    def succesor_traversal(self, p):
        i = 0
        while p != None:
            if i == 0:
                p = self.get_leftmost(p)
                i += 1
                #continue
            print(p.ele)
            if p.right:
                p = self.get_leftmost(p.right)
            else:
                wk = p
                while wk != wk.parent.left:
                    wk = wk.parent
                    if wk.parent == None:
                        break
                p = wk.parent

t = InorderTreversal()
for i in range(10):
    t.insert(i)


# Method 1: Recursion
# 7 3 8 1 9 4 0 5 2 6
print("Method 1: Recursion")
t.recurring_tranversal(t.root)

print("Method 2: Stack")
t.stack_traversal(t.root)

#print('Method 3: Successor')
#t.succesor_traversal(t.root)

print('Method 4: Morris')
t.morris_inorder(t.root)