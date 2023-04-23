# 깨달은 게 있는게 문제 보고나서 어디다가 적든 해서
# 원리를 보고 풀어야겠다.
# 그냥 문제만 쳐다보니까 당연히 어떻게 풀지 고민을 못하지
# 10의 제곱식으로 풀고있었는데, 써보기만 했어도 5로 풀었을 듯
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