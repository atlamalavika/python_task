# 1.Filter 
def positive_num(num):
    return num>0
list_val=eval(input("enter: "))
filter_val=filter(positive_num,list_val)
print(list(filter_val))

# 2
def funct(num):
    if num%2==0:
        return True
    else:
        return False
input_val=eval(input("enter: "))
result=filter(funct,input_val)
print(list(result))

#3 return vowels
def vowel_val(num):
    vowel=["a","e","i","o","u"]
    if num in vowel:
        return True
    else:
        return False
filter_num=eval(input("enter: "))
filter_val2=filter(vowel_val,filter_num)
print(list(filter_val2))