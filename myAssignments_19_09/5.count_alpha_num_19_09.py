# 5.write a rogram to count alphabets,digits,special characters in string
digits=0
alphabets=0
special_characters=0
given_string=input("enter_string: ")
for i in given_string:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        alphabets+=1
    else:
        special_characters+=1

print(digits)
print(alphabets)
print(special_characters)