# 1.remove given character from string
word=input("enter_value: ")
given_char=input("enter_char: ")
new_word=""
for i in word:
    if i==given_char:
        new_word+=""
    else:
        new_word=new_word+i
        
print(new_word)

#2 remove by replace
print(word.replace(given_char,""))