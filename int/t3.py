def t():
    try:
        return 1
    finally:
        return 2

print(t())
from collections import defaultdict
s = defaultdict(list)
#s[1] = []

s[1].append(2)
print(s)