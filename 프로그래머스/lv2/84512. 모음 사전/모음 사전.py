# 이런건 어떻게 생각하나 몰라
def solution(word):
    answer = 0
    word_dic = ['A', 'E', 'I', 'O', 'U']
    digit = [5**i for i in range(5)]
    for i in range(len(word)-1, -1, -1):
        tmp = word_dic.index(word[i])
        for j in range(5-i):
            answer += tmp*digit[j]
        answer += 1
    return answer

#중복 순열 이용
'''
from itertools import product

def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    lst = []
    
    for i in range(1, 6):
        for pr in product(words, repeat = i):
            lst.append("".join(pr))
            
    lst.sort()
    return lst.index(word) + 1
'''