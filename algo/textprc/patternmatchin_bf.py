
#time o(mn)
def bruthforce(str, sub):
    l1 = len(str)
    l2 = len(sub)

    for i in range(l1-l2+1):
        k = 0
        while k < l2 and str[i+k] == sub[k]:
            k+=1
        if k == l2:
            return i
    return -1


k = 'nameisrahul'
i = 'isr'

print(bruthforce(k,i))