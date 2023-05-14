

# def class add_sub
# 1 member constant: 5
# in it's constructor, it takes a boolean, which identifies whether we need to perform add or subtract
# and then it will have a method: called execute
# execute: will either add or subtract based on the constructor parameter
# and it will also add or subtract the constant that was pre-defined
# execute(num1, num2)
# num1 + num2 + constant if constructor param was True
# or, num1 - num2 - constant if constructor param was False
from typing import List
#import consta


class SingleTon(type):
    _dic = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._dic:
            inst = super(SingleTon, cls).__call__(*args, **kwargs)
            cls._dic[inst] = inst
        return cls._dic[cls]

class PL(metaclass=SingleTon):
    pass

o1 = PL()
o2 = PL()

print(id(o1), id(o2))


# class SingleTon(metaclass=type):
#     bool = True
#
#     def __new__(cls, *args, **kwargs):
#         if cls.bool:
#             return super().__new__(cls,*args, **kwargs)
#         return cls

o1 = SingleTon()
o2 = SingleTon()
print(id(o1), id(o2))

class AddSub:
    _connst = 5

    def __init__(self, type:bool=False):
        self._type = type

    def execute(self, num1: int, num2: int) -> int:
        if self._type:
            return num1 + num2 + self._connst
        else:
            return num1 - num2 - self._connst


class MultDiv(AddSub):
    def execute(self, num1: int, num2: int) -> int:
        if self._type:
            return num1 * num2 * self._connst
        else:
            return num1 / num2 / self._connst


#adition
ob = AddSub(True)
#ob.connst = 6
print('Add', ob.execute(1,4))
#pri

#substr
ob1 = AddSub()
print('Subs', ob1.execute(10,1))

ob2 = MultDiv(True)
print('Mult', ob2.execute(1,4))

ob3 = MultDiv()
print('Div', ob3.execute(1,4))


def test_mult_div():
    expected = 20
    ob2 = MultDiv(True)
    res = ob2.execute(1, 2)
    if res != expected:
        raise Exception('Invalid result')
    print('SUCCESS')


import unittest

test_mult_div()
