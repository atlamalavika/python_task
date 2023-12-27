# class Employee:
#     company="marolix"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name)
#         Employee.branch="python"
        
#     def method1(self,id):
#         self.id=id
#         print(self.id)
#         print(self.name)
#         print(Employee.company)
#     @classmethod
#     def classmethod(cls):
#         Employee.gender="female"
#         cls.value="sjhd"
#         print(Employee.key)
#         print(cls.gender)
#     @staticmethod
#     def staticmethod():
#         print(Employee.key)
#         Employee.key="jhkjsa"
        
#         print(Employee.key)
#         print(Employee.company)
# e1=Employee("malavika",20)
# e1.name="raj"
# e1.method1(101)
# Employee.night="jsjds"
# Employee.key="chanege"
# e1.classmethod()
# Employee.key="chanege"
# e1.staticmethod()

class Calculator:
    def method2(self):
        print("instamce")
    @classmethod
    def method(cls,x,y):
        print(x+y)
Calculator.method2()
Calculator.method(2,3)

