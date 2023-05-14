str1 = 'slkdhsajdhasldjksahda'
ar = [0]*256

dup = []
for i in range(len(str1)):
    if ar[ord(str1[i])] == 1:
        print(ord(str1[i]), ar[ord(str1[i])])
        dup.append(str1[i])
    ar[ord(str1[i])] = 1

print(ar)
print(dup)