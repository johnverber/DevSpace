#child grandchild relationship

#base or super class. note object in bracket.
#(generally obje is made ancestor in all classes)
#in python 3.x "class Person" is
# equivalent to "class Person (object)"

class Base(object):

    #Constructor
    def __init__(self, name):
        self.name = name 

    #to get name
    def getName(self):
        return self.name
    
#inherited or subclass (Note person in bracket)
class Child(Base):

    #constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def getAge(self):
        return self.age
    
#Inherited or Subclass (note person in bracket)
class GrandChild(Child):
    #constructor
    def __init__(self,name,age,address):
        Child.__init__(self,name,age)
        self.address = address

    #to get address
    def getAddress(self):
        return self.address 
    
g = GrandChild("John", 29, "Cocqui")
print(g.getName(), g.getAge(), g.getAddress())
