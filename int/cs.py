# n = input()
# n = str(n)
# n = 0
# su = 0
# for i in n:
#     su += int(i)
# # is_pel = str(su)

def is_pel(st):
    i = 0
    j = len(st) - 1
    le = len(st)
    if le < 2:
        return True
    while i < j:
        if st[i] != st[j]:
            return False
        i += 1
        j -= 1
    return True

#print(is_pel(str(su)))
# is_pel = str(sui)




a = [1,2,3,99,9,11]


#99932
outlist = []
#for i in a:
for i in range(len(a)):
    for j in range(len(a)):
        st = str(a[i]) + str(a[j])
        if str(a[j]) + str(a[i]) < str(a[i]) + str(a[j]):
            a[i], a[j] = a[j], a[i]
        #outlist.append(int(st))

print(a)
# print(outlist)
# srtli = sorted(outlist, reverse=True)
# print(srtli[0])

