# itertools 라이브러리에 permutations 함수를 사용하긴 했는데
# 하나하나 순열 진행하기에 조금 힘들 것 같아서 그냥 있을 법해서 함수를 쳐봤다.
# 근데 오히려 더 복잡하달까 사용법 알아두고 가면 좋을 것 같다.

from itertools import permutations

def solution(numbers):
    answer = 0
    primes = []
    for i in range(1, len(numbers)+1):
        primes.append(list(set(map(''.join, permutations(numbers, i)))))
    primes = list(set(map(int, set(sum(primes, [])))))
    
    print(primes)
    
    for i in primes:
        if i == 2 or i == 3:
            answer += 1
        if i > 3:
            tmp = 2
            while tmp < i:
                if i % tmp == 0:
                    answer -= 1
                    break
                else:
                    tmp += 1
            answer += 1
            
    return answer