#a= [32, 5, 3, 6, 7, 54, 87]

#Output: [3, 5, 6, 7, 32, 54, 87

li = [32, 5, 3, 6, 7, 54, 87]
n = len(li)
for i in range(n):
    for j in range(n):
        if li[i] < li[j]:
            li[i], li[j] = li[j], li[i]

print(li)
