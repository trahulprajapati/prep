from bstbase import BSTBase

class AVLTree(BSTBase):
    class Node(BSTBase.Node):
        def __init__(self, ele):
            super().__init__(ele)
            self.height = 0

        def right_height(self):
            return self.right.height if self.right else 0

        def left_height(self):
            return self.left.height if self.left else 0
    #find the unbalace tree
    # find the talk node
    #find  the gramchild weather its left or right
    #find rotation
    #rotate
    def re_calculate_height(self,p):
        p.height = 1+ max(p.left_height() , p.right_height())
    def is_inbalance(self, n):
        return abs(n.left_height() - n.right_height()) <= 1
        #return abs(n.left.height - n.right.height) <= 1
    def rebalance(self, x):
        y = x.parent
        z = y.parent

        if y == z.left and y.left == x:
            print('RR rotation')
            self.right_rotation(z)
            return y
            pass
        elif y == z.left and y.right == x:
            print('LR rotation')
            #left rotation(y)
            pass
            #right rotation(z)
        elif y == z.right and y.right == x:
            print('LL rotation')
            self.left_rotation(z)
            return y
            pass
            #left rotation
        elif y == z.right and y.left == x:
            print('RL rotation')
            pass
            #right rotation(y)
            #left rotation (z)
        else:
            print('invalida node ')
    def right_rotation(self, x):
        #copy
        x_par = x.parent
        y = x.left
        y_chi = y.right
        #relink
        y.right = x
        x.parent = y
        x.left = y_chi
        if y_chi:
            y_chi.parent = x
        y.parent = x_par

        if y.parent == None:
            self.root = y
        else:
            if y.parent.left == x:
                y.parent.left = y
            else:
                y.parent.right = y
        # self.re_calculate_height(x)
        # self.re_calculate_height(y)

    def left_rotation(self, x):
        #copy
        x_par = x.parent
        y = x.right
        y_chi = y.left
        #relink
        y.left = x
        x.parent = y
        x.right = y_chi
        if y_chi:
            y_chi.parent = x
        y.parent = x_par

        if y.parent == None:
            self.root = y
        else:
            if y.parent.left == x:
                y.parent.left = y
            else:
                y.parent.right = y


    def get_tall(self, p, flag):
        return p.left if p.left_height() + flag > p.right_height() else p.right

    #calcutlate the left chiuld or right child
    def get_grandchild(self, p):
        flag = 0
        chil = self.get_tall(p, 0)
        if chil == p.left:
            flag = 1
        return self.get_tall(chil, flag)

    def restructure(self, p):
        wk = p
        if wk.parent == None:
            return
        while p != None:
            oh = p.height #first time it will be 0
            if not self.is_inbalance(p):
                print( '==== in -- ', p.ele)
                p = self.rebalance(self.get_grandchild(p))
                self.re_calculate_height(p.left)
                self.re_calculate_height(p.right)
            self.re_calculate_height(p)
            if p.height == oh:
                p = None
            else:
                p = p.parent


t = AVLTree()

print('---##### Right rotation')
for i in range(5, 0, -1):
#for i in range(5):
    o = t.insert(i)
    t.restructure(o)
    print('===',o.ele)

t.print(t.root)
# nd = t.Node(9)
#print(nd.hight, nd.ele, nd.left)
print('---##### left rotation')

t2 = AVLTree()
for i in range(5):
    o = t2.insert(i)
    t2.restructure(o)
    print('===',o.ele)

t2.print(t2.root)
#print(t2.root.parent.ele)
#t = BSTBase()
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