from random import  choice
#return kth smallest element from unsorted list
#li = [3,6,2,7,4,9] , k = 3,, 3rd smallest element is -  4

#this is called prune and seach design pattern for every call size of li will be reduced
#time O(n), space O(n^2)

#second method will be sort and return k-1 index val from list

def quick_select(li, k):
    if len(li) == 1:
        return li[0]

    piv = choice(li)
    L = [i for i in li if i < piv ]
    E = [i for i in li if i == piv]
    G = [i for i in li if i > piv]

    if k <= len(L):
        return  quick_select(L, k)
    elif k <= len(L) + len(E):
        return piv
    else:
        kth = k - len(L) - len(E)
        return  quick_select(G, kth)


li = [3,6,2,7,4,9]
k = 3
print(quick_select(li, k))
