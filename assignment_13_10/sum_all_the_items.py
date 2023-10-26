#6.sum all the items in the dictionary
def sum_items(x):
    count=0
    for i in x:
        count=count+x[i]
    return count
dict=eval(input("enter: "))
print(sum_items(dict))