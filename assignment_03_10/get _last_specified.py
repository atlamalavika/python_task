#1 last element
word=eval(input("enter: "))
word1=list(word)
print(word1.pop())

#2 method 2
word1=eval(input("enter: "))
print(word1[-1])

#3 get specified element at index  from last element
index_value=int(input("enter: "))
word3=("malavika","rahul","shiva")
print(word3[-1][index_value])
