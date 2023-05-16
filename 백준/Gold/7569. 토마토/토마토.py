from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

que = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1: que.append([i, j, k])

def bfs(que):
    while que:
        x, y, z = que.popleft()

        for i in range(6):
            a = x+dx[i]
            b = y+dy[i]
            c = z+dz[i]

            if h>a>=0 and n>b>=0 and m>c>=0 and \
                graph[a][b][c]==0:

                que.append([a, b, c])
                graph[a][b][c] = graph[x][y][z] + 1

bfs(que)

ans = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                sys.exit(0)
        ans = max(ans, max(j))

print(ans-1)