#
# # class TestException(Exception):
# #     pass
# # i = 0
# # if not i :
# #     raise TestException('nooo')
#
def d1(p):
    def inn(func):
        print('in d1=======',p )
        def inner(*args):
            print(p)
            func(p+1)
            pass

        print('out d1---')
        return inner
    return inn


def d2(p):
    def inn(func):
        print('in d2======',p)
        def inner(*args):
            print(p)
            func(p+1)
            pass
        print('out d2-----')
        return inner
    return inn


def d3(p):
    def inn(func):
        print('in d3========', p)
        def inner(*args):
            print(p)
            func(p+1)
            pass

        print('out d3----------')
        return inner
    return inn

@d1(1)
@d2(10)
@d3(100)
def t(po):
    print('******', po)

t()

def p1(func):
    print('in p1 =======')
    def innner(*args):
        func()

    print('out p1**********')
    return innner

def p2(func):
    print('in p2 =======')
    def innner(*args):
        func()

    print('out p2**********')
    return innner

@p1
@p2
def t2():
    print('n testtttttttt')

t2()

# class Test:
#     def __init__(self, fun):
#         self.fun = fun
#     def __call__(self, fn):
#         print('====',)
#         def innner():
#             fn(self.fun)
#         return innner
#
# @Test(5)
# def pl(a):
#     print(a)
#
# pl()


# def test(fun):
#
#     def inner():
#         print('in d1')
#         fun()
#     return inner
#
# @test
# def t2(p):
#     print('innn d2')
#
# @t2
# def t3(p):
#     print('inn d3')
#
# t3()

