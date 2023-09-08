
#to show what will happen if you do not instantiate the 
#parent class within the child class or the child class within the parent
#class however your wanna look at it. 
class A:
    def __init__(self, n ='Rahul'):
        self.name = n

class B(A):
    def __init__(self, roll):
        self.roll = roll

object = B(23)
print(object.name)
