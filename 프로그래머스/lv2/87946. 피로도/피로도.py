#이건 다시 풀어보든가 해야할듯

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0 
        
        for req, tire in p:
            if tmp >= req:
                tmp -= tire
                cnt += 1
        answer = max(answer, cnt)
    return answer