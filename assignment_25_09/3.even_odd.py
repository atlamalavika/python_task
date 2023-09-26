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

#2
list2=eval(input("enter_list2: "))
even=[]
odd=[]
for i in list2:
    if i%2!=0:
        odd.append(i)
    else:
        even.append(i)
print(even)
print(odd)
