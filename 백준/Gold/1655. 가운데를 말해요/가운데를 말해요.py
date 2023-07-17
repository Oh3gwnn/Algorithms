import sys, heapq
input = sys.stdin.readline

n= int(input())
small, big = list(), list()

for _ in range(n):
    tmp = int(input())
    
    if len(small) == len(big): heapq.heappush(small, -tmp)
    else: heapq.heappush(big, tmp)

    if big and big[0] < -small[0]:
        heapq.heappush(small, -heapq.heappop(big))
        heapq.heappush(big, -heapq.heappop(small))

    print(-small[0])