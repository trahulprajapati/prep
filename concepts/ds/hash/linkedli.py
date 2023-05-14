
class LinkedList:
    class Node:
        def __init__(self, ele):
            self.ele = ele
            self.next = None
            self.prev = None

    def __init__(self):
        self.header = self.Node(None)
        self.tailer = self.Node(None)
        self.header.next = self.tailer
        self.tailer.prev = self.header
        self.cache = {}
        # nd = self.Node(None)
        # nd.next = self.tailer
        # nd.prev = self.header
        # self.header = nd
        # self.header = nd

        # self.header = self.Node(None)
        # self.tailer = self.Node(None)
        self.size = 0

    def insert_betwene(self, prev, next, ele):
        # if self.size == 0:
        #     next.p
        nd = self.Node(ele)
        nd.next = next
        nd.prev = prev
        prev.next = nd
        next.prev = nd
        self.size += 1
        self.cache[ele] = nd
        return nd

    def insert_top(self, ele):
        return self.insert_betwene(self.header, self.header.next, ele)

    def print(self):
        wk = self.header.next
        if self.size > 0:
            while wk != None:
                print(wk.ele, wk.prev.ele)
                wk = wk.next

class LRU:
    def __init__(self, s):
        self.size = s
        self.li = []# LinkedList()
        self.cache = {}

    def get(self,ele):
        if ele in self.cache:
            del self.li[ele]
            self.li.insert(0, ele)
            return self.cache[ele]
        return -1

    def put(self,ele):
        if ele in self.cache:
            del self.li[ele]
        self.li.insert(0, ele)
        self.cache[ele] = ele
        if len(self.cache) == self.size:
            ele = self.li.pop()
            del self.cache[ele]



ll = LinkedList()
li = [1,2,1,2,4,4,6]
for i in li:
    ll.insert_top(i)

#print(ll.header.ele,ll.header.next.ele,ll.header.next.next.ele)
#ll.print()

# for i in range(ll.size):
#     print()
print(len(ll.cache))
for i, j in ll.cache.items():
    print(j.ele)
