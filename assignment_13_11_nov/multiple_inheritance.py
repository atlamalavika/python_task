# Multiple inheritance : Inheriting multiple classes into single class at a time
class grandParent:
    def method1(self):
        self.grandfather="Bahubali"
class parent:
    def method2(self):
        self.father="Amerendra Bahubali"
class child(grandParent,parent):
    def method3(self):
        self.child="Mahendra Bahubali"
    def display(self):
        print("My grandfather -",self.grandfather)
        print("My Father -",self.father)
        print("My Name -",self.child)
object=child()
object.method1()
object.method2()
object.method3()
object.display()


