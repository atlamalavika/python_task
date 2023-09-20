# 7. Find sum of digits in string
string_with_digit=input("string_digit: ")
count=0
for i in string_with_digit:
    if i.isdigit():
        count+=int(i)
print(count)