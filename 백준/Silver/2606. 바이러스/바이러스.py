import sys
input = sys.stdin.readline

com, link = int(input()), int(input())
visited = [0 for _ in range(com + 1)]
links = [[] for _ in range(com + 1)]

for _ in range(link):
    x, y = map(int, input().split())
    links[x].append(y)
    links[y].append(x)

def bfs(n):
    que = [n]
    cnt = 0
    visited[n] = 1

    while que:
        tmp = que.pop(0)
        for j in links[tmp]:
            if visited[j] == 0:
                visited[j] = 1
                que.append(j)
                cnt += 1
    
    return cnt

print(bfs(1))