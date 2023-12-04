# a="a:1,b:1,c:2,c:5,b:2,d:4"
# a1=a.split(",")
# r={}
# for i in a1:
#     i1=i.split(":")
#     k,v=i1[0],int(i1[1])
#     print(k,v)
#     if k in r:
#         r[k]=r[k]+v
#     else:
#         r[k]=v
# print(r)

# a="python is a programming language"
# a1=""
# for i in a:
#     if i not in a1:
#         a1+=i
# print(a1)

# a="python is a launguage"
# a1=a.replace(" ","")
# print(a1)
# a=321
# a1=str(a)
# print(a1[::-1])
# a={}
# for i in range(2):
#   key=input("enter: ")
#   value=input("enter_vlue: ")
#   a[key]=value
# print(a)

# a={"a":1,"b":2,"c":3}
# check="v"
# k=list(a.keys())
# print(k)
# if check in k:
#     print(True)
# else:
# #     print(False)
# a={"a":1,"b":2}
# c={"c":3,"d":3}
# (a.update(c))
# print(a)

d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}

for i,j in d2.items():
    if i in d1:
        d1[i]=d1[i]+j
    else:
        d1[i]=j
print(d1)


