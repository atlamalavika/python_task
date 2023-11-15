#hybrid inheritance:combining more  than one type of inheritance
class company:
    def method1(self):
        self.company="marolix"
class domain(company):
    def method2(self):
        self.domain="python"
class employee(domain,company):
    def method3(self):
        self.name="ram"
    def method4(self):
        print("name",self.name)
        print("domain",self.domain)
e=employee()
e.method1()
e.method2()
e.method3()
e.method4()



