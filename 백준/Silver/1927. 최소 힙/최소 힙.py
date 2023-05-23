import heapq
import sys
input = sys.stdin.readline

n = int(input())
hp = []

for _ in range(n):
    tmp = int(input())
    
    if (tmp != 0): heapq.heappush(hp, tmp)
    else:
        try:
            print(heapq.heappop(hp))
        except:
            print(0)