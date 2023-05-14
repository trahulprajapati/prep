class Node:
    def __init__(self, d):
        self.ele = d
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add_level(self, ele):
        nd = Node(ele)
        if self.root == None:
            self.root = nd
            return
        pr = self.root
        qu = [pr]
        while True:
            p = qu[0]
            if p.left == None:
                p.left = nd
                break
            if p.right == None:
                p.right = nd
                break
            if p.left != None and p.right != None:
                qu.append(p.left)
                qu.append(p.right)
                qu.pop(0)

    def lvl_traversal(self):
        p = self.root
        q = [p]
        while len(q) != 0:
            p = q.pop(0)
            print(p.ele)
            if p.left != None:
                q.append(p.left)
            if p.right != None:
                q.append(p.right)

    def insert_binary(self, p, ele):
        if p == None:
            return Node(ele)
        if ele < p.ele:
            p.left = self.insert_binary(p.left, ele)
        elif ele > p.ele:
            p.right = self.insert_binary(p.right, ele)
        return p

    def inorder(self, p):
        if p:
            self.inorder(p.left)
            print(p.ele)
            self.inorder(p.right)

    def search(self, r, ele):
        if r.ele == ele:
            return r
        elif ele < r.ele:
            if r.left != None:
                return self.search(r.left, ele)
        else:
            if r.right != None:
                return self.search(r.right, ele)
        return r

    def insert_binary_iter(self, ele):
        nd = Node(ele)
        if self.root == None:
            self.root = nd
            return
        wk = self.root
        p = self.search(wk, ele)
        if p:
            if ele < p.ele:
                p.left = nd
            else:
                p.right = nd

    def insert_binry_iter2(self, ele):
        nd = Node(ele)
        if self.root == None:
            self.root = nd
            return
        wk = self.root
        prev = None
        while wk != None:
            if ele < wk.ele:
                prev = wk
                wk = wk.left
            else:
                prev = wk
                wk = wk.right

        if ele < prev.ele:
            prev.left = nd
        else:
            prev.right = nd

    def inorder_stk(self):
        p = self.root
        stk = []
        while len(stk) != 0 or p != None:
            if p != None:
                stk.append(p)
                p = p.left
            else:
                p1=stk.pop()
                print(p1.ele)
                p = p1.right

    def predecessor(self, p):
        if p == None:
            return
        prev = None
        if p.left:
            while p.left != None:
                p = p.left
        else:
            while p != None:
                prev = p
                p = p.left

    def inorder_succ(self):
        pass

    def inorder_morris(self):
        wk = self.root
        while wk != None:
            if wk.left:
                rm = wk.left
                while rm.right != None and rm.right != wk:
                    rm = rm.right
                if rm.right == None:
                    rm.right = wk
                    wk = wk.left
                else:
                    rm.right = None
                    print(wk.ele)
                    wk = wk.right
            else:
                print(wk.ele)
                wk = wk.right

    def preorder_stk(self):
        wk = self.root
        stk = [wk]
        while len(stk) != 0:
            el = stk.pop()
            print(el.ele)
            if el.right != None:
                stk.append(el.right)
            if el.left != None:
                stk.append(el.left)

    def preorder_morris(self):
        pass

    def postorder_stk(self):
        wk = self.root
        stk = [[wk, 0]]
        while len(stk) != 0:
            el, st = stk.pop()
            if el:
                if st == 1:
                    print(el.ele)
                else:
                    stk.append([el,1])
                    stk.append([el.right, 0])
                    stk.append([el.left, 0])

    def postorder_morris(self):
        pass

    def height_tree(self):
        pass

    def is_balanced(self):
        pass

    def successor(self):
        pass

# +++++++++++++++++++++++++++++++++++ R U N +++++++++++++++++++++++++++++++++++++++++++++++++
# p = Tree()
# for i in range(7):
#     p.add_level(i)
#
# p.lvl_traversal()
#

# p = Tree()
# p1 = p.insert_binary(p.root, 2)
# p1 = p.insert_binary(p1, 4)
# p1 = p.insert_binary(p1, 1)
# p1 = p.insert_binary(p1, 43)
# p1 = p.insert_binary(p1, 21)
# p1 = p.insert_binary(p1, 14)
#
# p.inorder(p1)
# 1
# 2
# 4
# 14
# 21
# 43

# p = Tree()
# for i in [2,4,1,43,21,14]:
#     p.insert_binary_iter(i)
#
# p.inorder(p.root)
#
# # 1
# # 2
# # 4
# # 14
# # 21
# # 43


p = Tree()
for i in [2,4,1,43,21,14]:
    p.insert_binry_iter2 (i)

#p.inorder(p.root)
# 1
# 2
# 4
# 14
# 21
# 43

#p.inorder_stk()
# 1
# 2
# 4
# 14
# 21
# 43

# p.inorder_morris()
# 1
# 2
# 4
# 14
# 21
# 43

# p.preorder_stk()
# 2
# 1
# 4
# 43
# 21
# 14

# p.postorder_stk()
# 1
# 14
# 21
# 43
# 4
# 2

