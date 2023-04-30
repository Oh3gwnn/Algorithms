import heapq

def solution(jobs):
    answer, time, i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= time:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = time
            time += cur[0]
            answer += (time - cur[1])
            i += 1
        else: time += 1
        
    return int(answer / len(jobs))