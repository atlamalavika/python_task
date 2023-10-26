#count upper and lower case characters
def count_char(x):
    upper=0
    lower=0
    for i in x:
        if i.isupper():
            upper+=1
        if i.islower():
            lower+=1
    print("No. of Upper case charaters : " +str(upper))
    print("No. of Upper case charaters : " +str(lower))    
input_string=input("enter: ")
count_char(input_string)