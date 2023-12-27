#1 remove char from string
# word="my name is malavika"
# char="a"
# word1=word.replace(char,"")
# print(word1)

#2 occurances of given chr in string
# word2="my name is malavika"
# char="a"
# print(word2.count(char))

# word3="my name is malavika"
# count=0
# char="m"
# for i in word3:
#     if i==char:
#         count+=1
# print(count)

# 3 strings are anagram
# a="silent"
# b="listen"
# if sorted(a)==sorted(b):
#     print(True)
# else:
#     print(False)

# count=0
# count1=0
# for i in a:
#     if i in b:
#         count+=1
# for i in b:
#     if i in a:
#         count1+=1
# if count==len(a) and count1==len(a):
#     print(True)
# else:
#     print(False)

# 4 string is palindrome or not
# word3="cat"
# word4=word3[::-1]
# if word3==word4:
#     print(True)
# else:
#     print(False)

# word5="mom"
# sol=""
# for i in range(len(word5)):
#     sol+=word5[len(word5)-i-1] 
# if word5==sol:
#     print(True)
# else:
#     print(False)

# 5 given char is vowel or consonant
# vowel="aeiou"
# char="a"
# if char in vowel:
#     print("vowel")
# else:
#     print("consonant")

#6 7 given char is digit or not
# chr="1"
# if chr.isdigit():
#     print(True)
# else:
#     print(False)
# chr=input()
# if chr>="0" and chr<="9":
#     print(True)
# else:
#     print(False)

#8 9 replace string space with a given character


# a="this is malavika"
# char="_"
# s1=a.replace(" ",char)
# print(s1)

# out2=""
# for i in a:
#     if i==" ":
#         out2+=char
#     else:
#         out2+=i
# print(out2)

# 10 convert lowecase char to uppercase of a string
# a="malaviKA"
# a1=a.upper()
# print(a1)

# ans=""
# for i in a1:
#     ans+=i.upper()
# print(ans)

#11 convert lowercase vowel to uppercase 
# word="my name is malavika"
# vowel="aeiou"
# sol=""
# for i in word:
#     if i in vowel:
#         sol+=i.upper()
#     else:
#         sol+=i
# print(sol)

#12 delete vowels in string
# word="malavika"
# vowel="aeiou"
# sol=""
# for i in word:
#     if i in vowel:
#         sol+=""
#     else:
#         sol+=i
# print(sol)

#13 count the occurances of vowels and consonants
# word="123malbbb"
# vow="aeiou"
# vowels=0
# consonants=0
# digits=0
# for i in word:
#     if i in vow:
#         vowels+=1
#     elif i.isalpha():
#         consonants+=1
#     else:
#         digits+=1
# print(vowels)
# print(consonants)
# print(digits)

# 14 highest frequency char in string
# word="malv"
# unique=""
# count={}
# for i in word:
#     if i not in unique:
#         unique+=i
#         count[i]=word.count(i)
# values=list(count.values())
# max_val=max(values)
# for i,j in count.items():
#     if max_val==1:
#         print(i)
#     else:
#         if max_val==j:
#             print(i)

# 15 first occurance of vowel with _
# a="malavika"
# vowel="aeiou" 
# a1=0
# for i in a:
#     if i in vowel:
#         a1=a.index(i)
#         break
# sol=""
# for i in range(len(a)):
#     if i==a1:
#         sol+="_"
#     else:
#         sol+=a[i] 
# print(sol)


# a="malavika"
# vowel="aeiou"
# a1=""
# for i in range(len(a)):
#     if a[i] in vowel:
#         a1=a[:i]+"_"+a[i+1:]
#         break
# print(a1)

#16 count alphabets,digits,special chars
# a="mala@#123"
# alpha=0
# digit=0
# special=0
# for i in a:
#     if i.isalpha():
#         alpha+=1
#     elif i.isdigit():
#         digit+=1
#     else:
#         special+=1
# print(alpha)
# print(digit)
# print(special)

#17 seperate charcaters in string
# a="mlavika yadav"
# str = "Hello Python"
# for char in str:
#     print(char)
#     print("\n")    
# str = "Hello Python"
# print("\n".join(list(str)))

#18 remove blank space from string
# a="my name is malavika"
# a1=a.replace(" ","")
# print(a1)

# b="malvika ya da v"
# b1=""
# for i in b:
#     if i==" ":
#         b1+=""
#     else:
#         b1+=i
# print(b1)

