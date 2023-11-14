# Hierarchical : Inheriting properties from single class into multiple classes
class Electronics:
    def __init__(self):
        print("Hi welcome to electronics world")
class Tv(Electronics):
    def method(self):
        print("Tv price is 25000")
class Ac(Electronics):
    def method1(self):
        print("AC price is 50000")
tv=Tv()
tv.method()
ac=Ac()
ac.method1()
