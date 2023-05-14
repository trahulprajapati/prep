

class Tree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, ele):
            self.ele = ele
            self.left = None
            self.right = None
            self.parent = None

    def create_tree(self, li):
        nd = self.Node(li[0])
        self.root = nd
        qu = []
        cn = self.root
        for i in range(1,len(li)):
            nd = self.Node(li[i])
            print('===', cn.ele, qu)
            if cn.left != None and cn.right != None:
                cn = qu.pop(0)
            elif cn.left == None:
                cn.left = nd
                print('=====', cn.ele)
                qu.append(nd)
            elif cn.right == None:
                cn.right = nd
                qu.append(nd)
    def level_orer(self):
        wk = self.root
        q = [wk]
        while len(q) != 0:
            cu = q.pop(0)

            ''


    # def levelorder(self):
    #     p = self.root
    #     q = [self.root]
    #     while len(q) != 0:
    #         nd = q.pop(0)
    #         if nd:
    #             print(nd.ele)
    #             if nd.left:
    #                 q.append(nd.left)
    #             if nd.right:
    #                 q.append(nd.right)


li = [1,2,3,4,5,6,7]
o = Tree()
o.create_tree(li)
o.levelorder()