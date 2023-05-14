class A:
    def m1(self):
        print('in m1')

    def m1(self,a):
        print('in m2')


class B(A):
    def m1(self):
        print('in m3')
a = B()
a.m1()