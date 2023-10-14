#10 merge 2 dictionaries
dict1={"emply1":"malavika","id":101,"salary":20000,"age":20}
dict2={"vill":"annaram","mndl":"manakondur"}
for i in dict2:
    dict1[i]=dict2[i]
print(dict1)