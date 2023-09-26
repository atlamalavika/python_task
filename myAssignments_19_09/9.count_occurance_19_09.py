# 9. write a program to count occurance of given character in string
string_with_occurance="malavikayadav"
occurance=input("string_occurance: ")
count=0
for i in string_with_occurance:
    if i==occurance:
        count+=1
print(count)    
