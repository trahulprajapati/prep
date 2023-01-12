class HeapSort(object):
    def __init__(self):
        self.li = [2,4,14,6,22,90,75,4,32]

    def left(self, i):
        return 2*i +1
    def right(self, j):
        return 2*j + 2

    def has_left(self, i , n):
        return self.left(i) < n
    def has_right(self, i , n):
        return self.right(i) < n

    def swap(self, i, j):
        self.li[i],self.li[j] = self.li[j],self.li[i]
    #heapify 1
    def heapify1(self, i, n):
        if self.has_left(i, n):
            mi = self.left(i)
            if self.has_right(i,n):
                r = self.right(i)
                if self.li[mi] > self.li[r]:
                    mi = r
            if self.li[mi] < self.li[i]:
                self.swap(mi,i)
                self.heapify1(mi, n)

    def heapify2(self, i, n):
        mi = i
        l = self.left(i)
        r = self.right(i)
        if l < n and self.li[l] > self.li[i]: # make > to < for descendin
            mi = l
        if r < n and self.li[r] > self.li[mi]:
            mi = r
        if mi != i:
            self.swap(mi, i)
            self.heapify2(mi, n)

    # time O(n logn) , space O(1)
    def heapsort(self):
        n = len(self.li)
        p = (n // 2) -1
        #o(logn)
        for i in range(p, -1, -1):
            #self.heapify1(i, n)
            self.heapify2(i, n)

        print(self.li)
        #o(n)
        for i in range(n-1, -1, -1):
            self.swap(0, i)
            #self.heapify1(0, i)
            self.heapify2(0, i)
        print(self.li)

s = HeapSort()
s.heapsort()