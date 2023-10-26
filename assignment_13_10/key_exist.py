# 2.check key exist in dictionary 
dict={"emply1":"malavika","id":101,"salary":20000,"age":20}
given_key=(input("enter: "))
print(given_key)
count=0
for i in dict:
    if i==given_key:
        count=count+1
if count==1:
    print("Given key exist in dictionary")
else:
    print("Given key does not exist in dictionary")
        
        
  
        

