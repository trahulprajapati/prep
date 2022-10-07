# O(m + n)
def compute_kmp(P):
    m = len(P)
    j = 1
    k = 0
    arr = [0] * m
    while j < m:
        if P[j] == P[k]:
            k += 1
            arr[j] = k
            j += 1
        elif k > 0:
            k = arr[k-1]
        else:
            j += 1
    print(arr)
    return arr

def kmpalgo(T, P):
    if len(P) == 0:
        return 0

    n = len(T)
    m = len(P)
    arr = compute_kmp(P)
    j = 0
    k = 0

    while j < n:
        if T[j] == P[k]:
            if k == m-1:
                print(j - k)
                k = arr[k-1]
            j += 1
            k += 1
        elif k > 0:
            k = arr[k-1]
        else:
            j += 1

T = 'dsdljkbbasdkjababababbabksaldjdlkadjababbab'
for i,j in enumerate(T):
    print(i,j)
P = 'ababbab'
kmpalgo(T, P)