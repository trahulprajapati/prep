


def replace(sno, dno, li):
    if len(li)<1:
        return
    for i in range(len(li)):
        if type(li[i]) == list:
            replace(sno,dno, li[i])
        else:
            if li[i] == sno:
                li[i] = dno

li = [5,10,[15,20, [25, 30, [35, 40, [45,50],55],60],65],70]
replace(30, 300, li)
print(li)
# sno = 30
# dno = 300
# # i = 0
# while i < len(li):
#     if type(li[i]) == list:
#         i=0
#         li = li[i]
#     else:
#         if li[i] == sno:
#             li[i] = dno
#         i+=1
# print(li)

st = ['abcd', 'efgh', 'ijkl', 'ggg']
def rev(stri):
    stli = list(stri)
    i =0
    j = len(stli)-1
    while i < j:
        stli[i], stli[j] = stli[j], stli[i]
        i+=1
        j-=1
    return ''.join(stli)


for i in range(len(st)):
    st[i] = rev(st[i])
print(st)

#x = lambda str: True if ['a','e', 'i','o', 'u'] in st else False
# lie = [True for i in st if ['a','e', 'i','o', 'u'] in st]
# print(lie)

def checkvov(str):
    for i in str:
        if i in ['a','e', 'i','o', 'u']:
            return True
    return False

# li = [checkvov(i) for i in st]
# print(li)
# # for i in st:
#     print(f'For {i}: ', checkvov(i))


class LL:
    class Node:
        def __init__(self, ele):
            self.next = None
            self.ele = ele

    def __init__(self):
        self.head = None

    def ad_ele(self, ele):
        nd = self.Node(ele)
        if self.head == None:
            self.head = nd
            return
        nd.next = self.head
        self.head = nd
#        se
    def print(self):
        wk= self.head
        while wk.next != None:
            print(wk.ele)
            wk = wk.next

#
# ll = LL()
# [ll.ad_ele(i) for i in range(5)]
# ll.print()



# with open('/Users/rahul.prajapati/rahul/prep/ws1/prep/file.txt') as fl:
#     for line in fl.readlines():
#         if 'def' in line:
#             #print(line)
#             infun = True
#         if infun:
#             print(line)
#         elif line == '':
#             infun = False