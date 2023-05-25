import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    que = deque([start])
    visited[start] = 1

    while que:
        tmp = que.popleft()
        for i in graph[tmp]:
            if visited[i] == 0:
                visited[i] = 1
                que.append(i)

cnt = 0

for i in range(1, n+1):
    if visited[i] == 0:
        if graph[i]: bfs(i)
        else: visited[i] = 1
        cnt+=1

print(cnt)