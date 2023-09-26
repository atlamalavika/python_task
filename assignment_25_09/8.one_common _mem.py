# 1 atleast one common factor
list1=eval(input("enter:list1: "))
list2=eval(input("enter:list2: "))
for i in list1:
    if i in list2:
        print("TRUE")
        break
    else:
        print("FALSE")
        break

# 2.[[1,2,3],[2,4,5],[1,1,1]] REMOVE A SPECIFIED COLUMN

list2=[[1,2,3],[2,4,5],[1,1,1]]
new_list=[]
index=eval(input("enter: "))
for i in list2:
    i.pop(index)
    new_list.append(i)
print(new_list)
