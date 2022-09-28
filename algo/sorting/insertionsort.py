#method 2: time O(n^2), o(m+n) space O(1)
def find_current_pos(li):
    for i in range(1, len(li)):
        cur = li[i]
        j = i
        while j > 0 and li[j-1] > cur:
            li[j] = li[j-1] #shifting
            j-=1
        li[j] = cur

li = [5,3,1,15,97,38,50]
print(li)
#print('mthod 1')
#insertion_sort(li)
print(li)
print('mthod 2')
find_current_pos(li)
print(li)
