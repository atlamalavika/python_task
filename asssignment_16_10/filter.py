# a=[1,2,4,5,6]
# a.reverse()
# count=0
# for i in range(2):
#     count+=a[i]
# print(count)

a=[1,2,3,4]
def square(num):
    return num*num
r1=map(square,a)
print(list(r1))