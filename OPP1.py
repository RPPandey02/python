# this show original class making
class test1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def doo(self):
        print("this is the 1st program")


x = test1(3, 2)
x.doo()


# now new test2 class will inherent from test1
class test2(test1):
    pass
