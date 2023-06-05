#
#
# From python3.7
# Run:
#     requement.txt
# COmmand:
#     /opt/python/bin activat
# expose 8080
# RUN:
# Hell.py runserver<>
#
#
# st, di
#
#
#
#

def demo1():
    print("Here no local variable  is present : ", locals())


# here local variables are present
def demo2():
    name = "Ankit"
    print("Here local variables are present : ", locals())
    print("Before updating name is  : ", name)

    # trying to change name value
    locals()['name'] = "Sri Ram"

    print("after updating name is : ", name)


# driver code
# demo1()
# demo2()

class Demo:
    @staticmethod
    def test(ob):
        ob.el = 90

o = Demo()
o.el = 10
print(o.el)
o.test(o)
print(o.el)