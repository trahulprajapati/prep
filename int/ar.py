# # def f(x,l=[]):
# #     l.append(x)
# #     return l
# #
# # print(f(1))
# # print(f(2))
# # print(f(3))
# #
# class A:
#    x = [1, 2, 3]
#
# class B(A):
#    pass
#
# class C(A):
#    x = [4, 5, 6]
#
# print(A.x)
#
# print(B.x)
#
# print(C.x)
#
# def make_adder(x):
#     def adder(y):
#         return x + y
#
#     return adder
#
#
# add_10 = make_adder(10)
#
# print(add_10(3))

#
# class Shape:
#
#     def __init__(self, x, y):
#         self.x = x
#
#         self.y = y
#
#         self.description = "This shape has not been described yet."
#
#     def description_setter(self, description):
#         self.description = description
#
#
# class Rectangle(Shape):
#
#     def __init__(self, x, y):
#         super().__init__(x, y)
#
#         self.description_setter("A rectangle can be described in terms of its width and height.")
#
#
# r = Rectangle(10, 20)
#
# print(r.description)

#TODO:1 Group Anagrams - https://leetcode.com/problems/group-anagrams/

# def group_ana(strs):
#     h= {}
#     #findalout = []
#     for e in strs:
#         r = sorted(e)
#         r = ''.join(r)
#         #e.sort()
#         print(r)
#         if r in h:
#             li = h[r]
#             li.append(e)
#         else:
#             print(r)
#             h[r] = [e]
#     #    h[r]
#     print(h)
#     final = []
#     for k,v in h.items():
#         final.append(v)
#     print(final)
#
# strs = ["eat","tea","tan","ate","nat","bat"]
# group_ana(strs)

#TODO:2 Group Anagrams - https://leetcode.com/problems/longest-substring-without-repeating-characters/

# def longest_substring(s):
#     ar = [0]*128
#
#     st = end = res = 0
#
#     while end < len(s):
#         r = s[end]
#         ar[ord(r)] += 1
#         while ar[ord(r)] > 1:
#             l = s[st]
#             ar[ord(l)] -= 1
#             st += 1
#         res = max(res, end-st+1)
#         end+=1
#     print(res)
# s = 'abcabcbb'
# longest_substring(s)

#TODO:3 Pat march brute force

# def bruthforce(t,p):
#     m = len(t)
#     n = len(p)
#
#     for i in range(m-n):
#         k = 0
#         while k < n and t[i+k] == p[k]:
#             k += 1
#         if k == n:
#             print('match', i)
#             break
#
#


# TODO:4 Pat march rabbitnkarp

# def matmatch_rabincarp(t, p):
#     m = len(t)
#     n = len(p)
#
#     di = {}
#     for i in range(n):
#         di[p[i]] = i
#
#     i = k = n-1
#     t = 'sjdhsakjdhkdhkjshd'
#     p = 'jdh'
#     while i < m:
#         if t[i] == t[k]:
#             if k == 0 :
#                 print('found')
#                 break
#             else:
#                 i-=1
#                 k-=1
#         else:
#             j = di.get(t[i], -1)
#             o = min(k, j+1)
#             i = i+n-o
#             k = n-1

# TODO:4 Letter Combinations of a Phone Number https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# def comb(list):
#
#     def dfs(res, comb, list):
#         res.append(comb)
#         for i in range(len(list)):
#             dfs(res, comb+[list[i]], list[i+1:])
#
#     res = []
#     dfs(res, [], list)
#     print(res)
#
#
# #inpit
# comb('23')
# #output-
# #[[], ['2'], ['2', '3'], ['3']]

# from collections import defaultdict
#
#
# class Graph:
#
#     # Constructor
#     def __init__(self):
#         # default dictionary to store graph
#         self.graph = defaultdict(list)
#
#     # function to add an edge to graph
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#
#
# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
#
# g.graph


_input = "abc"
_output = ""
def solve(ip,op):       # 3)c,  ab_c
    if not len(ip):
        print(op) #abc
        return
    op1 = op  #a. #ab, #abc_c

    op2 = op #a. #ab,  #abc_c
    op1 = op1 + ip[0] #    A + b, # ab + c, #ab_c,
    op2 = op2 + " " + ip[0] # a + + b, #ab + + c
    ip = ip[1: ] #c,
    solve(ip, op1) #c, ab, “‘“, abc
    solve(ip, op2) #c, ab c,

_output += _input[0] #a
_input = _input[1:] #bc
solve(_input, _output)