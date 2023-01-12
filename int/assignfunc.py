# def test():
#     def t1():
#         print('in t1')
#     def t2():
#         print('in t2')
#     def t3():
#         print('in t3')
#     t3.t1 = t1
#     t3.t2 = t2
#     return t3
#
# po = test()
# po()
# po.t1()
# #po.t2()

# class Test:
#     def di_in(self):
#         self.id =1
#         self.id2= 1
#         return self
#
#     @classmethod
#     def cl_m(cls):
#         return cls()
#         #print('in cls')
#         #return cls({1:1})
#     def ob_de(self):
#         return self
#
# class Test2(Test):
#     def t1(self):
#         print('in m2')
#
# o = Test2()
# o.id = 10
# print(o.__dict__, id(o))
# po = o.cl_m()
# po.id = 10
# ob2 = o.ob_de()
# print(po.__dict__, id(po), id(ob2))
#==========================================
# o1 = Test()
# print(id(o1), type(o1))
# pl = o1.di_in()
# pl.po=9
# print(id(pl), type(pl))
# print(pl.__dict__)
# o1.po = 10
# print(pl.__dict__)
#
# print(Test.cl_m())


from dataclasses import dataclass
import inspect

def ok(a,b,c):
    return True

#print(inspect.signature(ok))


@dataclass
class Test:
    p1: int = 0
    p2: str = ''
    p3: str = ''
    @classmethod
    def cm(cls, p1):
        pl = inspect.signature(cls).parameters
        di = {}
        for i,v in p1.items():
            if i in pl:
                di[i] =  p1[i]
        print(di)
        return cls(**di)
        #print('==',di)
        # for i, j in pl.items():
        #     print(f'{i, j.}')
        # #li = [v for v in inspect.signature(cls).parameters if v == param]
        #print(li)
        #return cls()
    def im(self):
        self.p1 = 40
        print('in im')
    @staticmethod
    def sm():
        print('in sm')
    # def t(self):
    #     print('in tttt')

# o = Test(p1=1,p2=2, p3=3)
# #print(o.__dict__, id(o))
# po = o.cm({'p1':1})
# po.p1
# print(po)

# o = Test()
# o2= o.cm({'p1':2})
# o2.im()
#
# print(o2.__dict__)
# print(o.__dict__, id(o))

from enum import Enum
class EnumEx(Enum):
    PR1 = 1
    PR2 = 2

o = EnumEx(2).name
print(o)
