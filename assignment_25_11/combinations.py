# def all_unique_combinations(words,n):
#     words=sorted(words)
#     items=list(range(len(words)))
#     old_combinations=[[]]
#     new_combinations=[]
#     for i in range(n):
#         new_combinations=[]
#         for combination in old_combinations:
#             for item in items:
#                 if (combination and  item >combination[-1]) or len(combination)==0:
#                     new_combinations.append(combination+[item])
#         old_combinations=new_combinations
#     word_combinations=[]
#     for combination in new_combinations:
#         word_combination=[]
#         for index in combination:
#             word_combination.append((words[index]))
#         word_combinations.append(tuple(word_combination))
#     return sorted(set(word_combinations))    
# words=input().split()
# words_len=len(words)
# for i in range(1,words_len+1):
#     all_combinations=all_unique_combinations(words,i)
#     for combination in all_combinations:
#         print(combination)

def unique_combinations(words,n):
    items=list(range(len(words)))
    old_combinations=[[]]
    new_combinations=[]
    for i in range(n):
        new_combinations=[]
        for combination in old_combinations:
            for item in items:
                if (combination and item>combination[-1]) or len(combination)==0:
                    new_combinations.append(combination+[item])
        old_combinations=new_combinations
    words_combinations=[]
    for combination in new_combinations:
        words_combination=[]
        for index in combination:
            words_combination.append(((words[index])))
        words_combinations.append(tuple(words_combination))
    return sorted(set(words_combinations))
words=input().split()
all_unique_combinations=unique_combinations(words,2)
for i in all_unique_combinations:
    print(*i)