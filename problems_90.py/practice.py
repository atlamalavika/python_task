# a=[1,2,3]
# b=a.copy()
# print(id(a))
# print(id(b))

# a=[[1,2,3],[2,3,4],[5,6,7]]
# count=0
# for i in a:
#     print(i[count])
#     count+=1

# a=[1,2,3,4,5,6]
# b=[i for i in a if i%2!=0]
# print(b)

# a=[1,2,3,4,1,2]
# b=sorted(a,reverse=True)
# print(b)

# a=(1,2,3)
# b,*c=a
# print(b)
# print(c)

# a=(1,2,3,4,5)
# b=(i for i in a if i%2==0)
# print(tuple(b))

# a={1,2,3,4}
# a.discard(2)
# print(a)

# a.discard(9)
# print(a)

# a={1,2,3,4}
# b={5,6,7,4}
# print(a.union(b))
# print(a|b)

# print(a.intersection(b))
# print(a&b)

# print(a.difference(b))
# print(a-b)

# print(a.symmetric_difference(b))
# print(a^b)

# a={101:"mala",102:"kav",103:"raj"}
# b={}
# for i in range(2):
#     key=input("enter: ")
#     value=input("enter: ")
#     b[key]=value
# print(b)

# def greet(name):
#     print("helo "+name)
# greet("manu")

# def wish(msg,name):
#     print("hi",name,msg)
# wish(name="good evening",msg="malavika")
# wish("praveen",name="mala")

# def defualt(name="mala"):
#     print("hello",name)
# defualt(name="yadav")
# defualt()  

# def display(**m):
#     for i,j in m.items():
#         print(i,j)

# display(id1=100,id2=200,id3=300)

# a=10
# def f1():  
#     global a
#     a=20
#     print(a)
# print(a)
# f1()
# print(a)

# def recur(num):
#     if num==1:
#         return 1
#     else:
#         return num*recur(num-1)
# a1=recur(2)
# print(a1)

# def fibo(num):
#     if num<=1:
#         return num
#     else:
#         return fibo(num-1)+fibo(num-2)
# a1=5
# for i in range(a1):
#     a1=fibo(i)
#     print(a1)

# a=[1,2,3,4,5]
# def posi(x):
#     return x>2
# a1=filter(posi,a)
# print(list(a1))

# s=lambda x,y,z:x+y
# s1=s(1,2,3)
# print(s1)

# p=lambda x,y:x if x%2==0 else y
# a1=p(2,3)
# print(a1)
# a=[1,2,3,4]
# def sqare(x):
#     return x*x
# a1=map(sqare,a)
# print(list(a1))
# a=[1,2,3,4]
# from functools import *
# def fun(x,y):
#     return x+y
# a1=reduce(fun,a)
# print(a1)

# lis=[1,2,3]
# s=lambda x,y:x+y
# s1=(reduce(s,lis))
# print(s1)
# res=reduce(lambda x,y:x+y,lis)
# print(res)

import functools
print(dir(functools))




