from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m:
                if lst[nx][ny] == 1:
                    lst[nx][ny] = lst[x][y] + 1
                    queue.append((nx, ny))

    return lst[n-1][m-1]

print(bfs(0, 0))