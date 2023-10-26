# REDUCE FUNCTIONS
from functools import *
list_value=[1,2,3,4]
result=reduce(lambda x,y:x+y,list_value)
print(result)
# 2
list_value=[1,2,3,4]
result=reduce(lambda x,y:x*y,list_value)
print(result)
# 3
list_value=[1,2,3,4]
def fun(x,y):
    return(x+y)

result=reduce(fun,list_value)
print(result)
