#1.even odd saperately
list1=eval(input("enter_list1: "))
even=[]
odd=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#2 list comprehension
even_list=[i for i in list1 if i%2==0]
print(even_list)
odd_list=[i for i in list1 if i%2!=0]
print(odd_list)
