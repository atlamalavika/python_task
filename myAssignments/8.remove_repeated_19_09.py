# 8. Remove repeated char from string
repeated=input("enter_repeated: ")
final_string=""
for i in repeated:
    count=0
    for j in repeated:
        if i==j:
            count=count+1
    if count==1:
        final_string+=i
print(final_string)     