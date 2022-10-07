#feb1
def feb1 (n):
    if n <= 1:
        return (n,0)
    a, b = feb1(n-1)
    return (a+b, a)

#feb2
def feb2(n):
    if n <= 1:
        return n
    return feb2(n-2) + feb2(n-1)
#feb3
def feb(n):
    li = [0,1]
    for i in range(n-1):
        li.append(li[-1] + li[-2])
    return li[-1]

print(feb(10))
print(feb2(10))
print(feb1(10))

