
ar1 = [4,1,2,1,1,2] #11
ar2 = [6,3,3,3] #15

ar1 = [6,1,2,1,1,2] #11
ar2 = [4,3,3,3] #15

# ar1 = [4,3,2,1,1,2] #13
# ar2 = [6,1,3,3] #13

# a1 = list(ar1)
# a2 = list(ar2)



for i in range(len(ar1)):
    f = 0
    for j in range(len(ar2)):
        tmp1 = list(ar1)
        tmp2 = list(ar2)
        tmp1[i], tmp2[j] = tmp2[j], tmp1[i]
        #if tmp1
        if sum(tmp1) == sum(tmp2):
            print(tmp1[i], tmp2[j], sum(tmp1), sum(tmp2) )
            f = 1
            break
    if f:
        break

print(ar1, ar2)
