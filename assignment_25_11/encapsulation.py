#Encapsulation : Bundling of methods and variables together 
#variables and methods can be public or private
#by default they are public we can accesse anywhere 
#if private we cannot access outside the class
class Encapsulation1:
    b=10 #public attribute
    _c=11 #protected attribute
    __d=12 #private atribute
    def __init__(self):
        self.__c=15
        print("this is constructor")
        print(Encapsulation1.b)
        print(Encapsulation1._c)
        print(Encapsulation1.__d)
    def method(self):
        print("This is parent class")
        print(Encapsulation1.b)
        print(Encapsulation1._c)
        print(Encapsulation1.__d)
obj=Encapsulation1()
print(obj.b)
print(obj._c)
# print(obj.__d) we cannot access private attribute outside the class 
print(obj._Encapsulation1__c)
obj.method()
print("______")


# class Encapsulation:
#     __a=10  #private variable
#     def method(self):
#         print("This is parent class")
#         print(Encapsulation.__a)
# obj=Encapsulation()
# # print(obj.a) :error
# obj.method()
