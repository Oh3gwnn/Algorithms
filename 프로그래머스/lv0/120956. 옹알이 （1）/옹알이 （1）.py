# 다시 풀어보기
from itertools import permutations as pe

def solution(babbling):
    s = ["aya", "ye", "woo", "ma"]
    words = []
    answer = 0
    
    for i in range(1, len(s)+1):
        for j in pe(s, i):
            words.append("".join(j))
    
    for i in babbling:
        if i in words:
            answer += 1
    
    return answer