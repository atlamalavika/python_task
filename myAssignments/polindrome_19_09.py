# 2.palindrome or not
palin_word=input("enter_palin: ")
reverse_word=palin_word[::-1]
if palin_word==reverse_word:
    print("It is a polindrome word")
else:
    print("It is not a palindrome word")