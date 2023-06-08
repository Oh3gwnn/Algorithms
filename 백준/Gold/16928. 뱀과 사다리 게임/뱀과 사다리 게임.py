from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [0 for _ in range(101)]
visited = [0 for _ in range(101)]


for _ in range(n+m):
    a, b = map(int, input().split())
    board[a] = b

def bfs(start):
    que = deque()
    que.append(start)

    while que:
        tmp = que.popleft()
        if tmp == 100:
            print(visited[100])
            break

        for i in range(1,7):
            if 100 >= i+tmp and visited[i+tmp] == 0:
                # 이전 방문 횟수랑 현재 방문 횟수 둘 중 작은거 넣어야 됨.
                # 이거까진 했는데 0일 때 처리를 못해서 자꾸 버벅
                if visited[i+tmp] == 0 or visited[i+tmp] > visited[tmp] + 1 :
                    visited[i+tmp] = visited[tmp] + 1
                if board[i+tmp]: 
                    que.append(board[i+tmp])
                    if visited[board[i+tmp]] == 0 or visited[board[i+tmp]] > visited[tmp] + 1 :
                        visited[board[i+tmp]] = visited[tmp] + 1
                else: 
                    que.append(i+tmp)

bfs(1)
