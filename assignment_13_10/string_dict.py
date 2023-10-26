#5.from string write dict with count of letters
given_dict="marolix technology"
result={}
for i in given_dict:
    if i!=" ":
        count_value=given_dict.count(i)
        result[i]=count_value
print(result)