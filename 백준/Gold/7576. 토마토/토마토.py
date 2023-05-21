from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
lst = [[i for i in map(int, input().split())] for _ in range(n)]

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

queue = deque()
result = 0

def bfs():
    while queue:
        tx, ty = queue.popleft()
        for k in range(4):
            dx = x[k] + tx
            dy = y[k] + ty

            if 0 <= dx < n and 0 <= dy < m:
                if lst[dx][dy] == 0:
                    lst[dx][dy] = lst[tx][ty] + 1
                    queue.append((dx, dy))

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            queue.append((i, j))

bfs()

for i in lst:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))

print(result-1)