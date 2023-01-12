# def li(ar, arr2):
#     if len(ar)<1:
#         return arr2
#     mx = max(ar)
#     arr2.append(mx)
#     i = ar.index(mx)
#     return li(ar[i+1:], arr2)
# A=[16,17,4,3,5,2]
# l1=li(A, [])
# print(l1)

# def a(*arg):
#     print('in a outer', arg)
#     #li = [1,2,3,3]
#     def b(*args):
#         print('in BBB')
#         print(args)
#         return [1,2,3]
#     b('callibg from A=====')
#     return b
#
# c = a('argsss')
# o  =c('outerrrr #######')
# print(o)
#



def test(a,b,*args):
    return a+b

def test2(func, st): # args pass
    print(st, 'in test2 function')
    def inner(a,b, *args):
        out = func(a,b)
        return out
    return inner # funtion return

var = test2(test, '=====')
print(var(1,2))