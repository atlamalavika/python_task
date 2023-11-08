#calculator
def call_common():
    numbers=input("enter_numbers").split()
    def convert_to_int(x1):
        return int(x1)
    num2=list(map(convert_to_int,numbers))#[1,2,3]
    return num2

def addition1():
    print("Add two number")
    r1=call_common()
    print(sum(r1))

def subtraction1():
    print("Difference of numbers")
    r1=call_common()
    print(r1[0]-r2[1])

def multiplication1():
    print("Multiplication of numbers")
    r1=call_common()
    result=1
    for i in r1:
        result=result*i
    print(result)

def division1():
    print("Division of numbers")
    r1=call_common()
    print(r1[0]/r1[1])

def modulus1():
    print("Reminder of number")
    r1=call_common()
    print(r1[0]%r1[1])

def power1():
    print("power of numbers")
    r1=call_common()
    print(r1[0]**r1[1])

input_value=int(input("enter_value: "))
if input_value==1:
    addition1()
elif input_value==2:
    subtraction1()
elif input_value==3:
    multiplication1()
elif input_value==4:
    division1()
elif input_value==5:
    modulus1()
elif input_value==6:
    power1()
