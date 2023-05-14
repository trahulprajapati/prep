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

    def insert3(self, ele):
        nd = self.Node(ele)
        par = None
        w = self.root
        while w != None:
            if ele < w.ele:
                par = w
                w = w.left
            else:
                par = w
                w = w.right
        # if par == None:
        #     par = nd
        if ele < par.ele:
            par.left = nd
        else:
            par.rigt = nd

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

    def successor(self, root, p):
        succ = None
        while root != None:
            if p.ele < root.ele:
                root = root.left
            elif p.ele > root.ele:
                succ = root
                root = root.right
            else:
                break
        return succ
    #
    def get_left(self, r):
        cur = r
        while cur.left != None:
            cur = cur.left
        return cur

    def inorder3(self, root):
        i = 0
        while root != None:
            if i == 0:
                root = self.get_left(root)
                i += 1
            print(root.ele)
            if root.right != None:
                root = self.get_left(root.right)
            else:
                temp =  root
                while temp != temp.parent.left:
                    temp = temp.parent
                    if temp.parent == None:
                        break
                root = temp.parent

    def inorder5_morris(self, root):
        r = root
        while r != None:
            if r.left != None:
                #find rightmost or cur == rightmost
                rm = r.left
                while rm.right != None and rm.right != r:
                    rm = rm.right
                #if rioiughmost == cur then rimost.right = Null , cur = cu.right
                if rm.right != None:
                    rm.right = None
                    print(r.ele, end=', ')
                    r = r.right
                # else rightmost = curerent , cur = cur.left
                else:
                    rm.right = r
                    r = r.left
            else:
                print(r.ele, end=', ')
                r = r.right

    def postorder(self, r):
        stk = [r, 0]
        while r != None:
            el, s = stk.pop()
            if r != None:
                if s == 1:
                    print(el.ele)
                else:
                    stk.append([r.left, 1])
                    stk.append([r.right, 0])
                    stk.append([r.left, 0])

    def print(self, e):
        print(e, end=', ')

    def preorder1(self, root):
        if root:
            #print(root.ele)
            self.print(root.ele)
            self.preorder1(root.left)
            self.preorder1(root.right)

    def get_min(self, r):
        w = r
        while w.left != None:
            w = w.left
        return w

    def delete1(self, r, k):
        if r == None:
            return
        if r.ele < k:
            r.left = self.delete1(r.left, k)
        elif r.ele > k:
            r.right =  self.delete1(r.right, k)
        else:
            if not r.left:
                tmp = r.right
                r = None
                return tmp
            if not r.right:
                tmp = r.left
                r = None
                return tmp

            tmp = self.get_min(r.right)
            r.ele = tmp.ele
            r.right = self.delete1(r.right, tmp.ele)
        return r

    # def delete2(self, r, k):
    #     if r.right:
    #         p = r
    #         s = r.right
    #         while s.left != None:
    #             p = s
    #             s = s.left
    #         if p != r:
    #             p.left = s.right
    #         else:
    #             p.right = s.right
    #
    #         r.ele = s.ele
    #         return r



t = Bst()
r= None
r = t.insert(r, 10)
r = t.insert(r, 50)
r = t.insert(r, 40)
r = t.insert(r, 14)
r = t.insert(r, 21)
r = t.insert(r, 1)
#print('t1 ======')
#t.inorder1(r)

li = [10,50,40,14,21,1]
for i in range(len(li)):
    t.insert2(li[i])
#print('t2 ======')
#t.inorder(t.root)

#t.inorder2()

#print('t3 ======')
#t.inorder5_morris(t.root)
print('rec')
#t.preorder1(t.root)
t.inorder5_morris(t.root)
print('===== 2==')
t.delete1(t.root, 10)
print('rec=== ')
t.inorder5_morris(t.root)

print('\n======ITER')
t2 = Bst()
li2 = [10,50,40,14,21,1, 100 , 100 ,1093]
nd = t2.Node(3)
t2.root = nd
for i in li2:
    t2.insert3(i)

t2.inorder5_morris(t2.root)
