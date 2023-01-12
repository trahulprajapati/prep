#inplace algo : time O(n logn) , space = o(1)
def quicksort_inplace(l, a, b):
    if a >= b:
        return

    #pivot
    p = l[b]
    le = a
    ri = b-1

    while le <= ri:
        while le <= ri and p > l[le]:
            le += 1
        while le <= ri and p < l[ri]:
            ri -= 1

        if le <= ri:
            l[le], l[ri] = l[ri], l[le] #swap
            le, ri = le, ri #shrink

    l[le], l[b] = l[b], l[le]

    #left
    quicksort_inplace(l, a, le-1)
    quicksort_inplace(l, le+1, b)

# time O(n^2) , #space O(n)
def quicksort(s):
    if len(s) < 2:
        return
    piv = s[-1]
    l = []
    g = []
    e = []
    for i in s:
        if i< piv:
            l.append(i)
        elif i > piv:
            g.append(i)
        else:
            e.append(i)
    quicksort(l)
    quicksort(g)
    s *= 0
    s.extend(l)
    s.extend(e)
    s.extend(g)

li = [2,4,7,1, 88,5,13,32,22]
print(li)
#quicksort(li)
quicksort_inplace(li, 0, len(li)-1)
print(li)