from collections import deque
import sys
input = sys.stdin.readline
mx = 100_001
n, k = map(int, input().split())
visit = [-1 for _ in range(mx)]
q = deque()

q.append(n)
visit[n] = 0

while q: 
    tmp = q.popleft()
    if tmp == k:
        print(visit[tmp])
        break
    if 0 < tmp*2 < mx and visit[tmp*2] == -1:
        visit[tmp*2] = visit[tmp]
        q.appendleft(tmp*2)
    if 0 <= tmp-1 < mx and visit[tmp-1] == -1:
        visit[tmp-1] = visit[tmp] + 1
        q.append(tmp-1)
    if 0 < tmp+1 < mx and visit[tmp+1] == -1:
        visit[tmp+1] = visit[tmp] + 1
        q.append(tmp+1)