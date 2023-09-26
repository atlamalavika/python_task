# 10. check string is anagrams or not in python
# First method
string1=input("enter_string1: ")
string2=input("enter_string2: ")
if sorted(string1)==sorted(string2):
    print("The strings are anagrams")
else:
    print("strings are not anagrams")
