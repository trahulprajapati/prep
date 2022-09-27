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
quicksort(li)
print(li)