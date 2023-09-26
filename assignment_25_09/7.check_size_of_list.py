# 1 check size of 2 list
list1=eval(input("enter:list1: "))
list2=eval(input("enter:list2: "))
if (len(list1)==len(list2)):
    print("size of 2 lists are same")
else:
    print("size of 2 lists are not same")


#2
count1=0
count2=0
for i in list1:
    count1+=1
for i in list2:
    count2+=1
if count1==count2:
    print("size of 2 lists are same")
else:
    print("size of 2 lists are not same")
