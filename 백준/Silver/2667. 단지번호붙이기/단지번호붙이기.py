from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

lst = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    lst[a][b] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < n:
                if lst[nx][ny] == 1:
                    lst[nx][ny] = 0
                    queue.append((nx, ny))
                    cnt += 1
    return cnt

count = []
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            count.append(bfs(i, j))
            
print(len(count))
for i in sorted(count): print(i)