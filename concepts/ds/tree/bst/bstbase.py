class BSTBase:
    class Node:
        def __init__(self, ele):
            self.ele = ele
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None

    def search(self, p, k):
        if p.ele == k:
            return p
        elif k < p.ele:
            if p.left != None:
                return self.search(p.left, k)
        else:
            if p.right != None:
                return self.search(p.right, k)
        return p

    def insert(self, k):
        nd = self.Node(k)
        if self.root == None:
            self.root = nd
            return self.root

        p = self.search(self.root, k)
        chi = p
        if p:
            if p.ele < k:
                nd.parent = p
                p.right = nd
                ch = p.right
            else:
                nd.parent = p
                p.left = nd
                ch = p.left
        return ch

    def get_lst(self,p):
        wk = p
        while wk.right != None:
            wk = wk.right
        return wk
    def before(self, p):
        if p.left != None:
            return self.get_lst(p.left)
        else:
            wk = p
            b4 = wk.parent
            while b4 != None and wk == b4.left:
                wk = b4
                b4 = wk.parent
            return b4

    def delete(self, k):
        p = self.search(self.root, k)
        if p.left and p.right:
            o = self.before(p)
            o.ele, p.ele = p.ele, o.ele
            p = o
        def children(c):
            if c.left != None:
                child = c.left
            else:
                child = c.right
            return child
        #if child:
        child = children(p)
        if p == p.parent.left:
            if child:
                child.parent = p.parent
                p.parent.left = child
            else:
                p.parent.left = None
        elif p == p.parent.right:
            if child:
                par = p.parent
                par.right = child
                child.parent = par
            else:
               p.parent.right = None
        else:
            print("---")
        #child.parent = p.parent

    def print(self, p):
        if p:
            self.print(p.left)
            print(p.ele,end=' parent: ')
            if p.parent != None:
                print(p.parent.ele)
            else:
                print(p.parent)
            self.print(p.right)

# t = BSTBase()
# t.insert(5)
# t.insert(1)
# t.insert(10)
# t.insert(100)
# t.insert(19)
# t.insert(3)
# t.print(t.root)

# t.delete(5)
# print('afterdelete ==')
# t.print(t.root)