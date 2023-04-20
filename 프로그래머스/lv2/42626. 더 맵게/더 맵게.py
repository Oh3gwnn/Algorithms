# 내가한거랑 로직 똑같은데 try except문 사용해서 진짜 깔끔하다.
# 근데 효율성(시간초과) 면에서 통과가 되지 않는데 그래서 다들 어쩔 수 없이
# heapq를 사용하는 것 같다.
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
# 힙은 자동정렬 기능이 추가되어있다.
import heapq

def solution(scoville, k):
    heap = []
        
    for num in scoville:
        heapq.heappush(heap, num)
    
    mix_cnt = 0
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1

    return mix_cnt