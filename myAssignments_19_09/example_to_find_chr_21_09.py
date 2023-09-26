i=input("enter: ")
if i.isalnum():
    print("alphabets or numbers")
    if i.isalpha():
        print("alphabet")
    else:
        print("number")
elif i.isspace():
    print("space")
else:
    print("special char")
    
    
