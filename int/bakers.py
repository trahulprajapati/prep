import random
from typing import List
class ValidaException(Exception):
    pass

a = 'programming'

occuracnce = {}
for i in a:
    if i in occuracnce:
        occuracnce[i] += 1
    else:
        occuracnce[i] = 1

print(occuracnce)

l1 = [1,2,3,4,1]
l2 = [5,6,7,8, 2, 4, 'sajk']

l6 = [lambda el: el*el for el in l1 if el%2==0]

#print(l6)
#  zip()
# di = d2 + d3

# l1= ['a', 'b', 'c']
# l2 = ['b','d', 'a']
#
# l3 = set(l1, l2)


import os


def gen():
    while True:
        yield random.Random(4)

for i in gen():
    print(i)

import time
def dec(func):
    def inner(*arg):
        print('Starting:', time.time())
        func()
        print('Ending:',time.time())
    return inner

@dec
def print_njmmm():
    print('in func')
    time.sleep(6)

print_njmmm()

class ListOperations:
    def __init__(self):
        self.li = ListClass()

    def multiple(self, l1 , l2):
        return self.li.validate_merge(l1,l2)

    def oper_complete(self, res):
        print(f'Operation Completed: {res}')

class ListClass:
    def __init__(self, op):
        self.op = op()
    temp = 5

    def validate_merge(self, l1: List, l2:List)-> List:
        ListClass.temp = 6
        #outlist = [l1[i] * l2[i] for i in range(len(l1))]
        #5,12,21,32
        leng = len(l1) if len(l1) < len(l2) else len(l2)
        outlist = []

        for i in range(leng):
            try:
                if i < len(l1) and i < len(l2):
                    if type(l1[i]) != int:
                        raise ValidaException('Invalida data')
                    ele = 0 if type(l1[i]) == str else l1[i]*l2[i]
                    outlist.append(ele)
                elif i < len(l1) and i > len(l2):
                    if type(l1[i]) != int:
                        raise ValidaException('Invalida data')
                    ele = 0 if type(l1[i]) == str else l1[i]
                    outlist.append(ele)
                else:
                    if type(l2[i]) != int:
                        raise ValidaException('Invalida data')
                    ele = 0 if type(l2[i]) == str else l2[i]
                    outlist.append(ele)
            except ValidaException as err:
                raise (err)

        ListOperations().oper_complete(outlist)
        return outlist


# print(ListClass.temp)
# ListClass.validate_merge(l1, l2)
# print(ListClass.temp)


