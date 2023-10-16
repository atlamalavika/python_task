#take a list and return distinct list
def distinct_list(x):
    new_list=[]
    for i in x:
        if i not in new_list:
            new_list.append(i)
    print(new_list)   
input_string=eval(input("enter: "))
distinct_list(input_string)