# #recursion 1 factorial
# def result(x):
#     if x==1:
#         return 1
#     else:
#         return x*result(x-1)
# num=int(input("enter: "))
# ans=result(num)
# print(ans)

# #2fibonacci series
# def result2(n):
#     if n<=1:
#         return n
#     else:
#         return result2(n-1)+result2(n-2) 

# num=int(input("enter: "))
# for i in range(num):
#     ans=result2(i)
#     print(ans)

# #sum of list:
# def sum_list(num_list):
#     if len(num_list)==1:
#         return num_list[0]
#     else:
#         return num_list[0]+sum_list(num_list[1:])
# num=eval(input("enter: "))
# print(sum_list(num))
 
def sum(lis):
    if len(lis)==1:
        return lis[0]
    else:
        return lis[0]+sum(lis[1:])
result=sum([1,2,3,4])
print(result)