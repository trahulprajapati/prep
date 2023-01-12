#
# n = input()
# n = str(n)
#
# su = 0
# for i in n:
# 	su += int(i)
#
# #is_pel = str(su)
# def is_pel(st):
# 	i = 0
# 	j = len(st)-1
# 	le = len(st)
# 	if le < 3:
#   		return True
# 	while i < j:
#   		if st[i] != st[j]:
# 	 		return False
#
# 	return True
#
# #is_pel = str(sui)
# print(is_pel(str(su))
class A:
	def do_t(self, i):
		print(type(self).__name__ , i)
		#print(type(self).__base__.__name__)
		def tu():
			pass

		print(tu.__doc__)
	def __call__(self, *args, **kwargs):
		params = kwargs if len(kwargs) else args
		print(params)

class B(A):
	pas = 10
	class PL:
		def po(self):
			print('call')

	def __call__(self, *args, **kwargs):
		params = kwargs if len(kwargs) else args
		#print('--', params)
		self.do_t(params[1])

	def do_t2(self):
		print(type(self).__base__.__name__)


ob = B()
ob(8,80)
# ob.t()
# ob.t2()
ls = getattr(ob, 'do_t')
#ls = getattr(ob, 'PL')
#ls = getattr(ob, 'pas')
ls(9)
#print(ls)
#print( getattr(ob, 'do_t'))