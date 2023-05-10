import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
t = int(input())

def bfs(lst, i, j):
    que = []
    que.append((i, j))
    lst[i][j] = 0

    while que:
        x, y = que.pop(0)

        for d in range(4):
            mx = x + dx[d]
            my = y + dy[d]

            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue

            if lst[mx][my] == 1:
                lst[mx][my] = 0
                que.append((mx, my))

for _ in range(t):
    cnt = 0
    n, m, k = map(int, input().split())
    lst = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        lst[x][y] = 1

    for i in range(n):
        for j in range(m):
            if lst[i][j] == 1:
                bfs(lst, i, j)
                cnt += 1

    print(cnt)