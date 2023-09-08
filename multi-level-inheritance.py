#multi-level-inheritance

#base class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

#intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername

        #invoking constructor of grandfather class
        Grandfather.__init__(self, grandfathername)

#derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname

        #invoking constructor of father class
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name: ', self.fathername)
        print('Son name: ', self.sonname)

#driver code
s1 = Son('Prince', 'Eden', 'John')
print(s1.grandfathername)
s1.print_name()

