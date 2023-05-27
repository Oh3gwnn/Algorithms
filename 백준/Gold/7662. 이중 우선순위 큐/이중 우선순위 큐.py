import heapq
import sys
input = sys.stdin.readline

t = int(input())

def findIdDelete(arr):
    while arr and id[arr[0][1]] == 0:
        heapq.heappop(arr)

for _ in range(t):
    heap_MAX, heap_MIN = [], []
    id = [0] * 1_000_000    
    k = int(input())

    for i in range(k):
        tmp = input().split()
        
        if tmp[0] == "I":
            heapq.heappush(heap_MAX, (-int(tmp[1]), i))
            heapq.heappush(heap_MIN, (int(tmp[1]), i))
            id[i] = 1

        elif tmp[0] == "D":
            if tmp[1] == "1":
                findIdDelete(heap_MAX)
                if heap_MAX:
                    id[heap_MAX[0][1]] = 0
                    heapq.heappop(heap_MAX)
                
            elif tmp[1] == "-1":
                findIdDelete(heap_MIN)
                if heap_MIN:
                    id[heap_MIN[0][1]] = 0
                    heapq.heappop(heap_MIN)

    findIdDelete(heap_MAX)
    findIdDelete(heap_MIN)

    if not heap_MIN: print("EMPTY")
    else: print(-heap_MAX[0][0], heap_MIN[0][0])