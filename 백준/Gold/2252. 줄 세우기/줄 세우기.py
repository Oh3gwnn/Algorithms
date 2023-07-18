import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = list([] for _ in range(n+1))
d = list(0 for _ in range(n+1))
q = deque()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    d[b] += 1

for i in range(1, n+1):
    if d[i] == 0: q.append(i)

ans = []
while q:
    tmp = q.popleft()
    ans.append(tmp)
    for i in graph[tmp]:
        d[i] -= 1
        if d[i] == 0: q.append(i)

print(*ans) # Asterisk(*) 리스트 압축 해제