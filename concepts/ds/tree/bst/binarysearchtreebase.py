class BinarySearchTreeBase:
    class Node:
        def __init__(self, ele):
            self.ele = ele
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None

    def left_most(self, p):
        if p is None:
            return p
        walk = p
        while walk.left is not None:
            walk = walk.left
        return walk

    def right_most(self, p):
        walk = p
        while walk.right is not None:
            walk = walk.right
        return walk

    def search(self, k, p):
        #if p:
        if p.ele == k.ele:
            return p
        if k.ele < p.ele:
            if p.left is not None:
                self.search(k, p.left)
        else:
            if p.right is not None:
                self.search(k, p.right)
        return p

    def insert(self, t, ele):
        nd = self.Node(ele)
        if self.root == None:
            self.root = nd
            return self.root
        p = self.search(nd, t)
        if nd.ele < p.ele:
            p.left = nd
        else:
            p.right = nd
        return p
    def insert_iter(self, key):
        nd = self.Node(key)
        if self.root == None:
            self.root = nd
            return

        walk = self.root
        prev = None

        while walk != None:
            if key < walk.ele:
                prev = walk
                walk = walk.left
            else:
                prev = walk
                walk = walk.right
        if prev.ele > nd.ele:
            prev.left = nd
        else:
            prev.right = nd

    def inorder(self):
        temp = self.root
        stack = []
        while (temp != None or not (len(stack) == 0)):
            if (temp != None):
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(str(temp.ele) + " ", end="")
                temp = temp.right
    def print_inter(self):
        walk = self.root
        temp = self.root
        stack = []
        stk = []
        #while len(stk) != 0:
        while (walk != None or not (len(stk) == 0)) :
            if walk != None:
                stk.append(walk)
                walk = walk.left
            else:
                walk = stk.pop()
                print(str(walk.ele) + " ", end="")
                walk = walk.right

    def print(self, p):
        if p:
            self.print(p.left)
            print(str(p.ele) + " ", end="")
            self.print(p.right)

    def delete(self, ele):
        walk = self.root
        p = self.search(ele, walk)
        walk = p
        parent = walk.parent
        while walk != None and walk == walk.parent.left:
            walk = parent
            parent = walk.parent
        #delete not check leaf  and delete

t = BinarySearchTreeBase()
t.insert_iter(4)
t.insert_iter(15)
t.insert_iter(8)
t.insert_iter(1)
t.insert_iter(87)
t.insert_iter(84)
t.insert_iter(38)
t.insert_iter(108)
t.insert_iter(68)
t.insert_iter(908)
t.print(t.root)
print('===')
t.print_inter()
print('===')
t.inorder()
# p = t.insert(t.root, 3)
# p = t.insert(p, 1)
# p = t.insert(p, 34)
# p = t.insert(p, 30)
# p = t.insert(p, 341)
# p = t.insert(p, 3431)
# p = t.insert(p, 3431)
# t.print(t.root)
# t.insert(310)
# t.insert(312)
# t.insert(301)
# t.print(t.root)





