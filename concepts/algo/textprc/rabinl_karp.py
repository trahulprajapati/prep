
p = 'rbababpsh'
d = 256
q = 105
h = 1

m = len(p)

h1  = 0
h2 = 0
# for i in p:
#     h2  += q * ord(i)
#     h1 = (d * h1 + ord(i)) % q
# print(h1, h2)

# for i in range(M):
#        p = (d*p + ord(pat[i])) % q
for i in range(len(p)-1):
    h = (d * h) % q
print(h)