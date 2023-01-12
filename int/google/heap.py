#find minimiun


class Heap:
    def __init__(self, li):
        self.li = li
        self.n = len(li)
    def left(self, n):
        return 2*n + 1
    def right(self, n):
        return 2*n+2

    def has_left(self, i, n):
        #return self.left(i) < len(self.li)
        return self.left(i) < n
    def has_right(self,i,n):
        #return self.right(i) < len(self.li)
        return self.right(i) < n
    def swap(self,i,j):
        self.li[i],self.li[j]=self.li[j],self.li[i]
    def heapify(self,i, n):
        if self.has_left(i,n):
            min = self.left(i)
            if self.has_right(i, n):
                ri = self.right(i)
                if self.li[ri] < self.li[min]:
                    min=ri
            if self.li[min] < self.li[i]:
                self.swap(i,min)
                self.heapify(min, n)
    def get_min(self):
        self.heapify(0, len(self.li))
        #print(self.li)
    def remove_min(self):
        self.get_min()
        self.swap(0, len(self.li)-1)
        v = self.li.pop(-1)
        self.heapify(0, len(self.li))
        #print(self.li)
        return v
    def extraspace_sort_heap(self):
        print(self.li)
        l2 = []
        for i in range(len(li)):
            l2.append(o.remove_min())
        print(l2)

    #def addnew(self):
    def inplace_heap_sort(self):
        print(self.li)
        n=len(self.li)
        p = n-1//2
        for i in range(p, -1 ,-1):
            self.heapify(i, n)
        print(self.li)
        for i in range(n-1, -1, -1):
            self.swap(0, i)
            self.heapify(0, i)
        print(self.li)

l2 = [34,5,2,75,29,26]
l2 = list(l2)
o = Heap(l2)
#o.extraspace_sort_heap()
o.inplace_heap_sort()

print('=-')
o2 = Heap([87,23,1,53,13,6,20])
o2.extraspace_sort_heap()
