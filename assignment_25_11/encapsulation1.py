# class MyClass:
#     def __init__(self):
#         self.public_var = "I am a public variable"
#         self._protected_var = "I am a protected variable"
#         self.__private_var = "I am a private variable"

#     def public_method(self):
#         print("This is a public method")

#     def _protected_method(self):
#         print("This is a protected method")

#     def __private_method(self):
#         print("This is a private method")

# class MySubClass(MyClass):
#     def __init__(self):
#         super().__init__()

#     def sub_class_method(self):
#         self.public_method()
#         self._protected_method()
        # self.__private_method() # This will raise an AttributeError

# obj = MySubClass()
# print(obj.public_var) # Output: I am a public variable
# print(obj._protected_var) # Output: I am a protected variable
# print(obj.__private_var) # This will raise an AttributeError
# obj.public_method() # Output: This is a public method
# obj._protected_method() # Output: This is a protected method
# obj.__private_method() # This will raise an AttributeError

class Parent:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30
    def method1(self):
        print("this is public")
    def _protected(self):
        print("this protected")
    def __private(self):
        print("this is private")
class Child(Parent):
    def __init__(self):
        super().__init__()
    def child_method(self):
        self.method1()
        self._protected()
        # self.__private()
obj=Child()
print(obj.a)
print(obj._b)
print(obj._Parent__c)

obj.child_method()
obj.method1()
obj._protected()
# obj.__private()
