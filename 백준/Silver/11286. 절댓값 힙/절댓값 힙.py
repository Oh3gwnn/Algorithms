import sys, heapq
input = sys.stdin.readline

n = int(input())
abs_heap = []

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(abs_heap, (abs(x), x))
    else:
        if abs_heap: print(heapq.heappop(abs_heap)[1])
        else: print(0)