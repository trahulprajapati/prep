#https://github.com/bfaure/Python3_Data_Structures/blob/master/AVL_Tree/main.py

def relink(self, parent, child, make_left_child):
    if make_left_child:
        parent.left = child
    else:
        parent.right = child
    if child is not None:
        child.parent = parent

def rotate(self, p):
    x = p.node
    y = x.parent
    z = y.parent
    if z is None:
        self.relink(z, x, y == z.left)
        self.root = x
        x.parent = None
    else:
        self.relink(z, x, y == z.left)
    if x == y.left:
        self.relink(y, x.right, True)
        self.relink(x, y, False)
    else:
        self.relink(y, x.left, False)
        self.relink(x, y, True)

def restructure(self, x):
    y = self.parent(x)
    z = self.parent(y)
    if (x == self.right(y)) == (y == self.right(z)):
        self.rotate(y)
        return y
    else:
        self.rotate(x)
        self. rotate(x)
        return x