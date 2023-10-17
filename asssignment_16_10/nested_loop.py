#Nested function
def outer():
    print("outer function")
    def inner():
        print("inner function")
    inner()
outer()

#2
def add(x):
    print(x+x)
    def square(x):
        print(x*x)
    print(x/2)
    square(x)
num=10
add(num)

# 3
def prime_num(x):
    count=0
    for i in range(2,x):
        if x%i==0:
            count+=1
    if count==0:
        print("prime number")
    else:
        print("Not a prime number")
    def even_num(x):
        if x%2==0:
            print("Even number")
        else:
            print("Odd number")
        def positive_num(x):
            if x>=0:
                print("Positive number")
            else:
                print("Negative number")
        positive_num(x)
    even_num(x)   
val=int(input("enter: "))
prime_num(val)
