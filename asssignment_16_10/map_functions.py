# 1 MAP
def square(x):
    return x*x
input_list=eval(input("enter: "))
result=list(map(square,input_list))
print(result)

#2
def square(x):
    return x+10
input_list=eval(input("enter: "))
result=list(map(square,input_list))
print(result)

#3
def square(x):
    if x>0:
        return x
input_list=eval(input("enter: "))
result1=list(map(square,input_list))
print(result1)