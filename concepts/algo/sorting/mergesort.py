#sequence
#time O(n logn) , space extra space o(n)

#method 1 LL
class LLQ:
    class Node:
        def __init__(self, ele):
            self.ele = ele
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def enqueue(self, ele):
        nd = self.Node(ele)
        if self.head == None:
            self.head = nd
            self.tail = nd
            self.n += 1
            return
        self.tail.next = nd
        self.tail = nd
        self.n += 1
    def dequeue(self):
        el = self.head.ele
        self.head = self.head.next
        self.n -= 1
        return el

    def print(self):
        wk = self.head
        while wk != None:
            print(wk.ele)
            wk = wk.next
    @property
    def is_empty(self):
        return self.n == 0
    @property
    def first(self):
        return self.head.ele

def mergel(s ,s1, s2):
    while not s1.is_empty and not s2.is_empty:
        if s1.first < s2.first:
            s.enqueue(s1.dequeue())
        else:
            s.enqueue(s2.dequeue())
    while not s1.is_empty:
        s.enqueue(s1.dequeue())
    while not s2.is_empty:
        s.enqueue(s2.dequeue())

def mergesortl(s):
    n = s.n
    if n < 2:
        return
    s1 = LLQ()
    s2 = LLQ()
    #print(n)
    while s1.n < n //2:
        s1.enqueue(s.dequeue())
    #print(n)
    while not s.is_empty:
        s2.enqueue(s.dequeue())

    mergesortl(s1)
    mergesortl(s2)

    mergel(s, s1, s2)


l = LLQ()
for i in reversed(range(5)):
   l.enqueue(i)

# l.print()
# mergesortl(l)
# print('afgter ')
# l.print()
# o = l.dequeue()
# l.print()
# print(o)


#method  2 Sequence
def mergesort(s):
    n = len(s)
    if n < 2:
        return
    mi = n // 2
    s1 = s[0:mi]
    s2 = s[mi:n]

    mergesort(s1)    #left
    mergesort(s2)    #right

    merge(s, s1, s2)


def merge(s, s1, s2):
    n = len(s)
    i = j = 0
    while i+j < n:
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]) :
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1

li = [1,4,2,45,22,11,0,44,7]
# print(li)
# mergesort(li)
# print(li)


#method 3 iteraticve
