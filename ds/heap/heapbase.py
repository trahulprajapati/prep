class HeapBase:
    class Item:
        def __init__(self, k, v, l):
            self.k = k
            self.v = v
            self.l = l

        def __lt__(self, other):
            return self.k < other.k

    def __init__(self):
        self.li = []

    def swap(self, i, j):
        self.li[i],self.li[j] = self.li[j], self.li[i]

    def is_empty(self):
        return len(self.li) == 0

    def left(self, i):
        return 2 * i + 1

    def has_left(self, i, n):
        return self.left(i) < n

    def right(self, i):
        return 2 * i + 2

    def has_right(self, i, n):
        return self.right(i) < n

    def uphead(self, i):
        p = (i-1) // 2
        if i > 0 and self.li[i] < self.li[p]:
            self.swap(i, p)
            self.uphead(p)

    def heapify(self, i, n):
        if self.has_left(i, n):
            mi = self.left(i)
            if self.has_right(i,n):
                ri = self.right(i)
                if self.li[ri] < self.li[mi]:
                    mi = ri
            if self.li[mi] < self.li[i]:
                self.swap(mi, i)
                self.heapify(mi, n)

    # def bubble(self, i):
    #     par = (len(self.li)-1) // 2
    #     if i > 0 and self.li[i] < self.li[par]:
    #         self.uphead(i)
    #     else:
    #         self.heapify(i, len(self.li)-1)

    def add(self, k, v):
        nd = self.Item(k, v, len(self.li))
        self.li.append(nd)
        self.uphead(len(self.li) -1)
        return nd

    def update(self, l, k, v):
        l.k = k
        l.v = v
        #self.bubble(id)
        self.heapify(0, len(self.li)-1)

    def remove_min(self):
        self.swap(0, len(self.li)-1)
        ele = self.li.pop()
        self.heapify(0, len(self.li)-1)
        return (ele.k, ele.v)

    def print(self):
        for i in self.li:
            print(f'{i.k} -- {i.v} -- {i.l}')

    @staticmethod
    def print_hash(di):
        for i in di:
            print(f'{i} : {di[i].k, di[i].v, di[i].l}' )

# h = HeapBase()
# di = {}
# for i in range(5, 1 ,-1):
#     di[i] = h.add(i, i+1)
#
# h.print_hash(di)
#
# print('Updating 3rd ele')
# h.update(di[3], 0, 100)
# h.print_hash(di)
#
# print("hashing-- ")
# h.print()
#
#
# print("remove mean ")
# pl, k = h.remove_min()
# print(pl, k)
# h.print()

# print("remove mean ")
# h.remove_min()
# h.print()

