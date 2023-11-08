#create an employee class and add details of employee  using three diferent 
#variables and access that variables in all possible ways

class Employee:
    company="Marolix" # declare static variable 1
    def __init__(self,name,id):
        self.name=name #instance variable 1 inside constructor
        self.id=id
        Employee.surname="Atla" # declare static variable 2
        print(self.work_type)
        print(self.name) #instance ACCESS 1
        print(Employee.surname) # STATIC access 1

    def method_1(self,domain):
        self.domain=domain #instance variable 2 inside instance method
        Employee.height="5.6" # declare static variable 3
        print(self.village)
        print(self.id)#instance ACCESS 2
        print(self.city)
        print(Employee.height) # STATIC access 2
      
        
    @classmethod
    def method_2(cls):
        Employee.salary=20000 # declare static variable 4
        cls.blood_group="O +ve"
        print(Employee.salary)# STATIC access 2.1
        print(cls.blood_group)#STATIC access 2.3
        
    @staticmethod
    def method_3():
        Employee.experience="2 years" # declare static variable 5
        print(Employee.experience)

    def local_method(self):
        greeting="Welcome" #Local Variable
        print(greeting)    #Local Variable ACCESS
        
Employee.work_type="Work from home"
obj_ref=Employee("Malavika","MT-02000")
Employee.city="hyderabad"
obj_ref.village="annaram" #instance variable 3 outside class using ORV
obj_ref.method_1("python")
print(obj_ref.domain)#instance ACCESS 3
obj_ref.method_2()
obj_ref.method_3()
print(Employee.company)# STATIC access 4
obj_ref.local_method()
