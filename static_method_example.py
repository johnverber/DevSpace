#static method

class MyClass:
    def __init__(self, value):
        self.value = value
        
    @staticmethod
    def get_max_value(x, y):
        return max(x,y)
    
#Create instance of myclass
obj = MyClass(40)

print(MyClass.get_max_value(20,30))
print(obj.get_max_value(20,30))