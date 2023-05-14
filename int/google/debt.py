
debts = [['Alex', 'Blake', 2],
         ['Blake', 'Alex', 2],
         ['Casey', 'Alex', 5],
         ['Blake', 'Casey', 7],
         ['Alex', 'Blake', 4],
         ['Alex', 'Casey', 4]
         ]

bh = {}
lh = {}

for i in range(len(debts)):
    if debts[i][0] in bh:
        bh[debts[i][0]] += debts[i][2]
    else:
        bh[debts[i][0]] = debts[i][2]
    if debts[i][1] in lh:
        lh[debts[i][1]] += debts[i][2]
    else:
        lh[debts[i][1]] = debts[i][2]

print(bh)
print(lh)
fl = {}
for k,v in bh.items():
    co = lh[k] - bh[k]
    if co < 0:
        fl[k] = lh[k] - bh[k]


print(fl)

