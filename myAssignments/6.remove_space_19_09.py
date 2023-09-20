# 6. Remove all blank spaces in string
word_with_blank=input("enter_value: ")
modified_string=""
for i in word_with_blank:
    if i==" ":
        modified_string+=""
    else:
        modified_string+=i
print(modified_string)