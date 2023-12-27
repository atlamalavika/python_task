#1 1-100 numbers one missing
# a=[]
# array_size=int(input("size_array: "))
# for i in range(array_size-1):
#     a1=int(input("enter: "))
#     a.append(a1)
# a2=list(range(array_size-1))
# print(a)
# print(a2)
# for i in a2:
#     if i not in a:
#         print(i)

# arr = []
# n = int(input("enter size of array : "))
# for x in range(n-1):
#     x=int(input("enter element of array : "))
#     arr.append(x)
# sum = (n*(n+1))/2;
# sumArr = 0
# for i in range(n-1):
#     sumArr = sumArr+arr[i];
# print(int(sum-sumArr)) 

#2 multiple numbers are there find duplicates
# arr=[]
# arr_size=5
# for i in range(arr_size-1):
#     i1=int(input("enter: "))
#     arr.append(i1)
# sol={}
# for i in arr:
#     if i not in sol:
#         if arr.count(i)>=2:
#             sol[i]=arr.count(i)
# for i,j in sol.items():
#     print(i, "is repeated ",j ,"times")

#3find all pairs sum equal to given num
# given_num=6
# arr=[1,2,3,4,5,6,7,8]
# sol=[]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if (arr[i]+arr[j])==given_num:
#             sol.append((arr[i],arr[j]))
# print(sol)

#4 compare arrays in equal size or not
# a=[1,2,3,4]
# b=[1,2,3]
# if len(a)==len(b):
#     print(True)
# else:
#     print(False)
#5 find smallest nd largest num in array
# a=[1,2,3,4,5]
# print(min(a))
# print(max(a))

# greatest=a[0]
# small=a[0]
# for i in a:
#     if i>greatest:
#         greatest=i
#     if i<small:
#         small=i
# print(greatest)
# print(small)
#6 2nd highest num in array
# a=[1,2,3,4,5,6]
# a1=sorted(a,reverse=True)
# print(a1[1])

# greatest=a[0]
# small=a[0]
# for i in a:
#     if i>greatest:
#         greatest=i
#     if i<small:
#         small=i
# greatest1=small
# for i in a:
#     if  i!=greatest  and i>greatest1:
#         greatest1=i
# print(greatest1)

#7 2 maximum numbers
# a=sorted([1,2,3,4,1,2])
# a.reverse()
# print(a[0])
# print(a[1])

#8 remove duplicete elements from array
# a=[1,2,3,3,4,4,5]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
#9 top 2 maximum num in array
#10 arraya in reverse order
# a=[1,2,3,5]
# a1=(a.reverse())
# print(a)
# sol=[]
# for i in range(len(a)):
#     a2=a[len(a)-i-1]
#     sol.append(a2)
# print(sol)

#11 reverse array in 2 ways
# a=[1,2,3,5]
# a1=(a.reverse())
# print(a)
# sol=[]
# for i in range(len(a)):
#     a2=a[len(a)-i-1]
#     sol.append(a2)
# print(sol)

#12 claculate len(array)
# a=[1,2,3,4,5]
# print(len(a))

#13 insert element at end of array
# a=[1,2,3,4]
# a.append(7)
# print(a)

#14 insert element at given location in array
# a=[1,2,3,4]
# a.insert(2,9)
# print(a)

#15 delete element at end of the array
# a=[1,2,3,4]
# a.pop()
# print(a)

#16 delete given element from array
# a=[1,2,3,4,5]
# a.remove(2)
# print(a)

#17 delete element at given index
# index=3
# a=[1,2,3,4,5]
# a.pop(index)
# print(a)
# del a[2]
# print(a)

#18 sum of array elements
# a=[1,2,3]
# print(sum(a))

#19 20 all even num in arry
# a=[1,2,3,4,5,6]
# even=[]
# odd=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)

#21 perform left rotation of array elemts by 2 positions
# a=[1,2,3,4,5]
# val=int(len(a)/2)
# print(a[val:]+a[:val])

# a1=[1,2,3,4,5]
# a1.append(a1.pop(0))
# a1.append(a1.pop(0))
# print(a1)

#22 perform right rotation of array elemts by 2 positions
# a=[1,2,3,4,5]
# val=int(len(a)/2)
# print(a)
# print(a[val:]+a[:val]) #left rotation
# print(a[-val:]+a[:-val])

#23 merge 2 arrays
# a=[1,2,3]
# a1=[4,5,6]
# print(a+a1)
# a.extend(a1)
# print(a)

#24 highest frequency element in array
# a=[1,2,3,4,4,4,6,7,7,7,5]
# sol={}
# for i in a:
#     if i in sol:
#         sol[i]=sol[i]+1
#     else:
#         sol[i]=1
# print(sol)
# values=max(list(sol.values()))
# for i,j in sol.items():
#     if j==values:
#         print(i)

#25 ADD TWO NUMBERS USING RECURSION
# def add(num1,num2):
#     if num2==0:
#         return num1
#     else:
#         return add(num1 ^ num2, (num1 & num2) << 1)
# a1=add(10,22)
# print(a1)