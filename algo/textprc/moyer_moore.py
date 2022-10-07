
# O(mn)
def pattern_search(T, P):
    if len(P) == 0:
        return 0
    n = len(T)
    m = len(P)

    #map patterns char in dict
    di = {}
    for i in range(m):
        di[P[i]] = i

    i = m-1
    k = m -1
    print(di)
    while i < n:
        #matched case
        if T[i]== P[k]:
            if k == 0:
                #print(i)
                return i
            else:
                i -= 1
                k -= 1
        else: #not matched
            #check if char is exist in dict
            j = di.get(T[i], -1)
            print('--jk-- ', j, k)
            #reset value of i where to shift
            i += m - min(k, j+1)
            print('--i --',i)
            k = m-1
    return -1

P = 'abc'
T = 'asdkldjabaklsjasklablaksjaklsacsdacsdsadabc'
print(pattern_search(T, P))
