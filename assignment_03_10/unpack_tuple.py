#1unpacking tuple
words=eval(input("enter_tuple: "))
print(words)
emp1,emp2,emp3,emp4=words
print(emp1)
print(emp2)
#2
words2=eval(input("enter_tuple: "))
emp1,*emp2=words2
print(emp1)
print(emp2)