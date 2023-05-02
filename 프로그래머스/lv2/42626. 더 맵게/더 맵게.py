# 내가한거랑 로직 똑같은데 try except문 사용해서 진짜 깔끔하다.
# 근데 효율성(시간초과) 면에서 통과가 되지 않는데  
# 그래서 heapq를 사용하는 것 같다.
'''
def solution(scoville, k):
     mix_cnt = 0
     while min(scoville) < k:
         scoville.sort()
         try:
             scoville.append(scoville.pop(0) + (scoville.pop(0) * 2))
         except IndexError:
             return -1
         mix_cnt += 1

     return mix_cnt
'''
# 힙은 2k+1 정렬이 들어간 맨 앞자리 최소 값 배열 같은 느낌이다.
# sort의 정렬 비용을 감소시킨다.

# 이해하기 위해서 다시 풀어본 코드
import heapq

def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    
    while 1:
        min_sco = heapq.heappop(scoville)
        if min_sco >= k: break
        if not scoville: return -1
        sec_sco = heapq.heappop(scoville)
        heapq.heappush(scoville, min_sco + sec_sco*2)
        
        answer += 1

    return answer