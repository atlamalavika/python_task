#1.remove duplicates from list
list1=eval(input("enter:list1: "))
new_list=[]
for i in list1:
    if list1.count(i)==1 or i not in  new_list:
        new_list.append(i)
print(new_list)
