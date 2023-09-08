#demostration of private members

class C(object):
    def __init__(self):
        self.c = 21

        #d is a private instance variable
        self.__d = 42

class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)

object1 = D()

#produces an error as d is a private instance variable
print(object1.c)
print(object1.__d)
