#recursion 1 factorial
def result(x):
    if x==1:
        return 1
    else:
        return x*result(x-1)
num=int(input("enter: "))
ans=result(num)
print(ans)

#2fibonacci series
def result2(n):
    if n<=1:
        return n
    else:
        return result2(n-1)+result2(n-2) 

num=int(input("enter: "))
for i in range(num):
    ans=result2(i)
    print(ans)


