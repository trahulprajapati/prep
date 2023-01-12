class TreeBase:
    class Node:
        def __init__(self, ele):
            self.ele = ele
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, ele):
        nd = self.Node(ele)
        if self.root == None:
            self.root = nd
            return
        st = [self.root]
        while True:
            el = st[0]
            if el.left == None:
                el.left = nd
                break
            elif el.right == None:
                el.right = nd
                break
            elif el.left and el.right:
                st.append(el.left)
                st.append(el.right)
                st.pop(0)

    def level_trevrsl(self):
        q = [self.root]
        while len(q) != 0:
            el = q.pop(0)
            print(el.ele)
            if el.left:
                q.append(el.left)
            if el.right:
                q.append(el.right)

    def inorder(self, p):
        if p:
            self.inorder(p.left)
            print(p.ele, end=" ")
            self.inorder(p.right)

    def get_leftmost(self,p):
        while p.left != None:
            p = p.left
        return p

    def get_rightmost(self,p):
        while p.right != None:
            p = p.right
        return p
# t= TreeBase()
# for i in range(10):
#     t.insert(i)

#t.level_trevrsl()

# print('==')
# t.inorder(t.root)