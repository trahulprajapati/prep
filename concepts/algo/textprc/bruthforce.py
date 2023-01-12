T= 'BSLKJASKLJFDSJFJCAACNAKJHSGADBLJAACASDHBASD'
P = 'AAC'
n = len(T)
m = len(P)
for i in range(n-m + 1):
    k = 0
    while k < m and T[i+k] == P[k]:
        k += 1
    if k == m:
        print('matchned ', i)




