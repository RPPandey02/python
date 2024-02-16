# multiple level inheretance
class x:
    def __init__(self, a):
        self.a = a

    def ts(self):
        print('1st prog')


class y(x):
    pass


class z(y):
    pass


# normal variable are pulilc
# variable with '_' at beingging are protected
# variable with "__" at start are private
class abc:
    def __init__(self, p, q, r):
        self.p = p
        self._q = q
        self.__r = r

    def tts(self):
        print('1st prog')

obj1=abc(10,25,65)

print(obj1.p)
print(obj1._q)
print(obj1._abc__r)
