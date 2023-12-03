#Encapsulation : Bundling of methods and variables together 
#variables and methods can be public or private
#by default they are public we can accesse anywhere 
#if private we cannot access outside the class
class Encapsulation1:
    b=10
    def __init__(self):
        print("this is constructor")
    def method(self):
        print("This is parent class")
obj=Encapsulation1()
print(obj.b)
obj.method()
print("______")

class Encapsulation:
    __a=10  #private variable
    def method(self):
        print("This is parent class")
        print(Encapsulation.__a)
obj=Encapsulation()
# print(obj.a) :error
obj.method()
