import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) # dfs 반복 횟수 제한 해제

v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    n = list(map(int, input().split()[:-1]))
    for i in range(1, len(n)-1, 2): graph[n[0]].append((n[i], n[i+1]))

def dfs(x, y):
    for a, b in graph[x]:
        if visited[a] == -1:
            visited[a] = b+y
            dfs(a, b+y)

visited = [-1] * (v+1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1] * (v+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))