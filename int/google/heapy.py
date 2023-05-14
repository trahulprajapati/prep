

class Heap:
    def __init__(self, li):
        self.li = li

    def has_left(self,i, n):
        return 2 * i+1 < n
    def has_right(self, i, n):
        return 2*i+2 < n
    def left(self, i):
        #return  self.li[2*i+1]
        return 2*i+1
    def right(self, i):
        #return self.li[2*i+2]
        return 2*i+2
    def parent(self,i):
        return i-1//2
    def swap(self, i, j):
        self.li[i],self.li[j] = self.li[j], self.li[i]
    def heapify(self, i, n):
        if self.has_left(i, n):
            mi = self.left(i)
            if self.has_right(i,n):
                ri = self.right(i)
                if self.li[ri] < self.li[mi]:
                    mi = ri
            if self.li[mi] < self.li[i]:
                self.swap(i, mi)
                self.heapify(mi, n)


li = [324,23,23,6,22,1,435,21]
ob = Heap(li)
print(ob.li)
n = len(li)
p = n -1 // 2
for i in range(p, -1, -1):
    ob.heapify(i, n)

for i in range(n-1, -1, -1):
    ob.swap(0, i)
    ob.heapify(0, i)
print(ob.li)



