
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

t = "9812654321023213"

# i = 0
# j = 1
# for i in range(n):
#     if
# def isvalid(arr, n):
#     for i in range(n - 3):
#         j = i + 1
#         f = 1
#         while (int(arr[i]) + 1) == int(arr[j]):
#             f += 1
#             i += 1
#             j += 1
#             if f == 5:
#                 return 1
#     return -1


def isvalid(arr, n):
    for i in range(n - 1):
        j = i + 1
        f = 1
        while int(arr[i]) == (int(arr[j]) + 1):
            f += 1
            i += 1
            j += 1
            if f == 4:
                return 1
    return -1


arr = list(t)
print(isvalid(arr, len(arr)))

# f = t%10
# p = f//10
# print(p)
# #s=
# t = t//10
# print(t, f)

# f = %10
# p = f//10
# print(p)
# #s=
# t = t//10
# print(t, f)
# out = 0
# while t != 0:
