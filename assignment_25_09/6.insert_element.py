# 1.insert element at index
list1=eval(input("enter:list1: "))
index1=int(input("num: "))
char=eval(input("char: "))
list1.insert(index1,char)
print(list1)

#2
list2=eval(input("enter:list2: "))
index2=int(input("num: "))
char2=eval(input("char: "))
new_lst1=list2[:index2]
new_list2=list2[index2:]
print(new_lst1+[char2]+new_list2)

