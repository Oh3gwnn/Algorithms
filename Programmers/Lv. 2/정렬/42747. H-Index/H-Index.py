# 처음에 문제 이해를 못했는데(설명이 이상하다는 평이 많음)
# 위키백과 링크 있길래 그거 보니까 그냥 풀려버렸다.

def solution(citations):
    a = 0
    answer = 0
    for i in range(1, len(citations)+1):
        for j in citations:
            if j >= i:
                a += 1
        print(a)
        if a >= i:
            answer += 1
            a = 0
        else:
            return answer
    return answer