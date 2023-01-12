#method 1: time O(n^2), space O(1)
def selection_sort(li):
    l = len(li)
    for i in range(l):
        mi = i
        for j in range(i+1, l):
            if li[j] < li[mi]:
                mi = j
        li[mi],li[i] = li[i], li[mi]

li = [5,3,1,15,97,38,50]
selection_sort(li)
print(li)