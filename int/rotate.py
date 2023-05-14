#
# shift = 2
# encoder = {}
#
# for k in range(26):
#     encoder[k] = chr((k + shift) % 26 + ord( 'A' ))
#     #decoder[k] = chr((k − shift) % 26 + ord( 'A' ))
# print(encoder)

ar = [1,2,3,4,5]
k = 2
ar2 = list(ar)
len = len(ar)
for i in range(len):
    ar[i] = ar2[(i+k)%len]

print(ar)