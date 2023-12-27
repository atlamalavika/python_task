# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name)
#     def method1(self):
#         print(self.name)
#         print(self.age)
# class Student(Person):
#     def __init__(self,name,age,gender):
#         super().__init__(name,age)
#         self.gender=gender
#         print(self.gender)
#     def method1(self):
#         super().method1()
#         print(self.gender)

# ob1=Student("malavika","20","female")
# ob1.method1()

# class Parent:
#     a=10
#     def __init__(self):
#         self.name="malavika"
# class Child(Parent):
#     def method(self):
#         print(self.name)
#         print(super().a)
# e1=Child()
# e1.method() 
class Student:
    def __init__(self,maths):
        self.maths=maths
    def __mul__(self,internal):
        return self.maths * internal
c1=Student(30)
c2=Student(20)
print(c1*c2)
