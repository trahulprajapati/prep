class P:
    def add(self):
        print('in one')
    def add(self, x):
        print('in two')
    def hs(self):
        h = {1:1, 3:3}
        for i, j in h.items():
            print(i,j)
p = P()
#p.add()
p.hs()