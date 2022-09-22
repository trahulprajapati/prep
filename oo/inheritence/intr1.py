class T:
    __slots__ = 'r'
    def __init__(self):
        self.f = None
        self.h = None

class T2(T):
    #__slots__ = 'i'
    def __init__(self):
        self.p = None
        #super().__init__()

o = T2()
print(o.i)