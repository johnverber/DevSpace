#parent class
class Person(object):
    # constructor
    def __init__(self,  name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
        
#child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        #invoking  the init of the parent of class
        Person.__init__(self,name,idnumber)

a = Employee('John', 884012, 200000, "Stud Muffin")
a.display()