#delete  first given element from list
list1=eval(input("enter:list1: "))
char=(input("num: "))
if char.isdigit():
    char=int(char)
list1.remove(char)
print(list1)

#2 
list2=eval(input("enter:list2: "))
char2=(input("num: "))
if char2.isdigit():
    char2=int(char2)
for i in list2:
    if i==char2:
        list2.remove(char2)
        break
print(list2)
