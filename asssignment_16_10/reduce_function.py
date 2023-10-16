# REDUCE FUNCTIONS
from functools import *
list_value=[1,2,3,4]
result=reduce(lambda x,y:x+y,list_value)
print(result)

list_value=[1,2,3,4]
result=reduce(lambda x,y:x*y,list_value)
print(result)

list_value=[1,2,3,4]
result=reduce(lambda x,y:x/y,list_value)
print(result)