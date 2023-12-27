#19 concetenate 2 strings using join()
# a="word"
# a1="string"
# a2="".join([a,a1])
# print(a2)

#20 conctatinate 2 strings 
# print(a+a1)

#21 remmove repeated char from string
# a="mynameismal"
# a1=""
# for i in a:
#     if i not in a1:
#         a1+=i
# print(a1)

#22 calculate sum of integers
# num=0
# a="malvika@1231"
# for i in a:
#     if i.isdigit():
#         num+=int(i)
# print(num)

#23 not repeating chr in string
# a="malavika yadav"
# b=""
# for i in a:
#     if a.count(i)==1:
#         b+=i
# print(b)

# a="malavika"
# sol={}
# for i in a:
#     if i in sol:
#         sol[i]+=1
#     else:
#         sol[i]=1
# sl=""
# for i in sol:
#     if sol[i]==1:
#         sl+=i
# print(sl)

#24 copy one string to another string
# a="malavika"
# b=""
# for i in a:
#     b+=i
# print(id(a))
# print(id(b))

#25 sort char of string in ascending ordr
# a="malavika"
# a1=(sorted(a))
# print("".join(a1))

#26 sort  chr of dtring in descending order
# a="malavika"
# a1=sorted(a,reverse=True)
# print("".join(a1))

a=(input())
b=(input())
print(a/b)