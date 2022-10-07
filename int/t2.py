
def sub(s):
    i = 0
    di = {}
    out = ""
    arr = []
    while i < len(s):
        if i == len(s)-1:
            arr.append(out)
        if s[i] in di:
            arr.append(out)
            out = ""
        else:
            di[s[i]] = 1
            out += s[i]
        i += 1
    arr.sort()
    print(arr)
    print(arr[-1])
    print(len(arr[-1]))

s = "abcdxyzxb"
s2 = "abcdabcbbxyzt"
s3 = "pwwkew"
sub(s)
sub(s2)
sub(s3)