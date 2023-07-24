import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q, p = deque(), deque()
    q.append((0,0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if board[nx][ny] == 0: q.append((nx, ny))
                elif board[nx][ny] == 1: p.append((nx, ny))

    for x, y in p:
        board[x][y] = 0
    return len(p)

n, m = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
board = list()
cnt = 0

for i in range(n):
    board.append(list(map(int, input().split())))
    cnt += sum(board[i])
t = 1

while 1:
    visited = [[0]*m for _ in range(n)]
    tmp = bfs()
    cnt -= tmp
    if cnt == 0:
        print(t, tmp, sep='\n')
        exit(0)
    t += 1