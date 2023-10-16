#Find sentence is pangram or not
def distinct_list(x):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    count=0
    for i in alphabet:
        if i in x:
            count+=1
    if count==26:
        print("Given string is a Pangram")  
    else:
        print("Given string is not a Pangram")
input_string=eval(input("enter: "))
distinct_list(input_string)