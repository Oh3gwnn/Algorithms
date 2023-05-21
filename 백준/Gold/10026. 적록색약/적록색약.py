from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

lst = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res1, res2 = 0, 0
que = deque()

def bfs():
    while que:
        x, y = que.popleft()
        visited[x][y] = 1
        
        for i in range(4):
            kx = x + dx[i]
            ky = y + dy[i]
            if (0 <= kx < n) and (0 <= ky < n) and visited[kx][ky] == 0:
                if lst[x][y] == lst[kx][ky]:
                    visited[kx][ky] = 1
                    que.append([kx, ky])

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            que.append([i, j])
            bfs()
            res1 += 1

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if lst[i][j] != 'B': lst[i][j] = 'N'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            que.append([i, j])
            bfs()
            res2 += 1

print(res1, res2)