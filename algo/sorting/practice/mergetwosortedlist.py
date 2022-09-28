l1 = [1,3,5,7,9,11]
l2 = [0,2,4,6,9]

le = len(l1) + len(l2)
i = j = 0
#l = [None]*le
l = []
#p = [None]*le
#mwrthod 1
while l1 and l2:
    if l1[0] < l2[0]:
        l.append(l1.pop(0))
    else:
        l.append(l2.pop(0))
while l1:
    l.append(l1.pop(0))
while l2:
    l.append(l2.pop(0))
#method 2
# while i+j < le:
#     if j == len(l2) or (i<len(l1) and l1[i] < l2[j]):
#         l.append(l1[i])
#         p[i+j] = l1[i]
#         i += 1
#     else:
#         l.append(l2[j])
#         p[i + j] = l2[j]
#         j += 1

print(l)
#print(p)