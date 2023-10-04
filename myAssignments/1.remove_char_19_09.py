# 1.remove given character from string
word1=input("enter_value: ")
given_char=input("enter_char: ")
new_word=""
for i in word1:
    if i==given_char:
        new_word+=""
    else:
        new_word=new_word+i
print(new_word)