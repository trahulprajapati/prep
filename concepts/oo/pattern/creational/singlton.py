class SingTonClass(type):
    obs = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.obs:
            cl = super().__call__(*args, **kwargs)
            cls.obs[cls] = cl
        return cls.obs[cls]

class Test(metaclass=SingTonClass):
    pass

o1 = Test()
o2 = Test()
print(id(o1), id(o2))