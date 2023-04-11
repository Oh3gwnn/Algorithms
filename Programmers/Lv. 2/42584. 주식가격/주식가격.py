# 정확성 10/10, 효율성 0/5
'''
def solution(prices):
    answer = []
    
    while prices:
        tmp = 0
        x = prices.pop(0)
        
        for i in prices:
            tmp += 1
            if x > i:
                break
        answer.append(tmp)
        
    return answer
'''

# stack 풀이
def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)]
    
    tmp = [0]
    
    for i in range(1, len(prices)):
        while tmp and prices[tmp[-1]] > prices[i]:
            j = tmp.pop()
            answer[j] = i - j
        tmp.append(i)
    return answer

# deque
# 아니 그놈의 데큐가 뭐길래 다들쓰나 했는데
# 원래 안되던 맨 위 코드가 되게한다.
# 근데 이거 써도 되는거야? 얼탱이밤탱이네 완전

from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        tmp = 0
        x = prices.popleft()
        
        for i in prices:
            tmp += 1
            if x > i:
                break
        answer.append(tmp)
        
    return answer