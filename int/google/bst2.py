
class BST:
    class Node:
        def __init__(self, ele):
            self.ele = ele
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None

    def search(self, p, k):
        if p == None:
            return p
        if p == k:
            return p
        elif k <= p.ele:
            return self.search(p.left, k)
        elif k >= p.ele:
            return self.search(p.right,k)
        return p

    def insert(self, p, ele):
        nd = self.Node(ele)

        p = self.search(p, ele)
        ch = None
        if ele < p.ele:
            p.left = nd
            nd.parent = p
            ch = nd

