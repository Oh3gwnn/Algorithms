import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    tmp = -int(input())

    if tmp != 0:
        heapq.heappush(heap, tmp)
    else:
        try: print(-heapq.heappop(heap))
        except: print(0)