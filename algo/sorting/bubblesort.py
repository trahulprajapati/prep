#method 1: time O(n^2), space O(1)
def insertion_sort(li):
    while True:
        i = 0
        j = len(li)-1
        fl = 0
        while i < j:
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
                fl = 1
            i += 1
        if not fl:
            break
li = [5,3,1,15,97,38,50]
