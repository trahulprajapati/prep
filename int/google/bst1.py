class Bst:
    class Node:
        def __init__(self,ele):
            self.ele = ele
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, root, e):
        if root == None:
            return self.Node(e)
        if e <= root.ele:
            root.left = self.insert(root.left,e)
        elif e >= root.ele:
            root.right = self.insert( root.right, e)
        return root

    def search(self, k, r):
        if k == r.ele:
            return r
        elif k < r.ele:
            if r.left != None:
                return self.search(k, r.left)
        else:
            if r.right != None:
                return self.search(k, r.right)
        return r
    def insert2(self, ele):
        nd = self.Node(ele)
        if self.root == None:
            self.root = nd
            return self.root
        p = self.search(ele, self.root)
        if ele < p.ele:
            p.left = nd
        else:
            p.right = nd

    def inorder1(self, r):
        if r:
            self.inorder1(r.left)
            print(r.ele)
            self.inorder1(r.right)

    def inorder2(self):
        st = []
        nd = self.root
        while nd != None or len(st) != 0:
            if nd != None:
                st.append(nd)
                nd = nd.left
            else:
                el = st.pop()
                print(el.ele)
                nd = el.right


t = Bst()
r= None
r = t.insert(r, 10)
r = t.insert(r, 50)
r = t.insert(r, 40)
r = t.insert(r, 14)
r = t.insert(r, 21)
r = t.insert(r, 1)
print('t1 ======')
t.inorder1(r)

li = [10,50,40,14,21,1]
for i in range(len(li)):
    t.insert2(li[i])
print('t2 ======')
#t.inorder(t.root)

t.inorder2()



