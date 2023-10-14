# 7 combine 2 dictionaries by adding values for common keys
d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}
result={}
for i in d1:
    if i in d2.keys():
        result[i]=d1[i]+d2[i]
    else:
        result[i]=d1[i]
        for i in d2:
            if i not in d1:
                result[i]=d2[i]
print(result)
