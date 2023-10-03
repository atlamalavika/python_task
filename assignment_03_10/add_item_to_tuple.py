#1 add items to tuple concatination
word1=eval(input("enter: "))
word2=eval(input("enter: "))
print(word1+word2)

#2 update value at particular index
word3=eval(input("enter: "))
converted_word=list(word3)
converted_word[3]="india"
print(tuple(converted_word))

#3 add item at index
word4=eval(input("enter: "))
converted_word=list(word4)
converted_word.insert(2,"india")
print(tuple(converted_word))