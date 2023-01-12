class Tree:
    class Node:
        def __init__(self, ele):
            self.left = None
            self.right = None
            self.ele = ele

    def __init__(self):
        self.root = None

    # def add_left(self, ele, p):
    #     nd = self.Node(ele)
    #     if self.root == None:
    #         self.root = nd
    #         return
    #     if p.left:
    #         raise ValueError("already exext", p.left.ele)
    #     p.left =
    def inorder(self, p):
        if p:
            self.inorder(p.left)
            print(p.ele, end=', ')
            self.inorder(p.right)

t = Tree()
n1 = t.Node(1)
n2 = t.Node(2)
n3 = t.Node(3)
n4 = t.Node(4)
n5 = t.Node(5)
n6 = t.Node(6)
n7 = t.Node(7)

t.root=n1
t.root.left = n2
t.root.right = n3
t.root.left.left = n4
t.root.left.right = n5
t.root.left.left.left = n6
t.root.left.left.left.left = n7

t.inorder(t.root)