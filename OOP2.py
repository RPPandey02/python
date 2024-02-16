# Now case happen when a class inherent two class function and variable

# Originally, all  function can inherent but variable from 1st class only inherited

class xy:
    def __int__(self, a, b):
        self.a = a
        self.b = b

    def test1(self):
        print("this 1st prog")

    def test2(self):
        print("this 2nd prog")


class yz:
    def __int__(self, p, q):
        self.p = p
        self.q = q

    def test1(self):
        print("this 1st prog")

    def test2(self):
        print("this 2nd prog")

# now this third class will inherent and with properly in a differently
class xyz(xy,yz):
    pass

obj=xyz()


