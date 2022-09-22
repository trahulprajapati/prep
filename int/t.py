
n = input()
n = str(n)

su = 0
for i in n:
	su += int(i)
  
#is_pel = str(su)
def is_pel(st):
	i = 0
	j = len(st)-1
	le = len(st)
	if le < 3:
  		return True
	while i < j:
  		if st[i] != st[j]:
	 		return False
      
	return True

#is_pel = str(sui)
print(is_pel(str(su))
