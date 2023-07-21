import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def bfs(x, y):
  cnt = 0
  q = deque()
  visited[x][y] = 1 
  q.append((x, y))
  
  while q:
      x, y = q.popleft()
      for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
          nx, ny = x + dx, y + dy 

          if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
              if board[nx][ny] != 'X':
                  q.append((nx, ny))
                  visited[nx][ny] = 1
                  if board[nx][ny] == 'P':
                      cnt += 1
  return cnt         
               
for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            cnt = bfs(i, j)
            
if cnt != 0:
    print(cnt)
else:
    print('TT')