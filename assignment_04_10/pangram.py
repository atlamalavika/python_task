#Find sentence is pangram or not
def distinct_list(x):
    x1=x.lower()
    alphabet="abcdefghijklmnopqrstuvwxyz"
    count=0
    for i in alphabet:
        if i in x1:
            count+=1
    if count==26:
        print("Given string is a Pangram")  
    else:
        print("Given string is not a Pangram")
input_string=(input("enter: "))
distinct_list(input_string)