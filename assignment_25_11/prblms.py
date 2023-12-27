# from abc import ABC,abstractmethod
# class Test1(ABC):
#     @abstractmethod
#     def  method1(self):
#         pass
# class Test2:
#     def m2(self):
#         print("jshjd")
# t=Test2()
# t.m2()


try:
    a=(input())
    b=(input())
    print(a/b)
except ZeroDivisionError:
    print("jsdhjs")
except ValueError:
    print("values")
except TypeError:
    print("type")



        
