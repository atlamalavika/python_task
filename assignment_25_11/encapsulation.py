#Encapsulation : Bundling of methods and variables together 
class Encapsulation1:
    def __init__(self):
        print("this is constructor")
    def method(self):
        print("This is parent class")
obj=Encapsulation1()
obj.method()

class Encapsulation:
    __a=10  #private variable
    def method(self):
        print("This is parent class")
        print(Encapsulation.__a)
obj=Encapsulation()
obj.method()
