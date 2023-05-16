import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    cnt = [0] * (n+1)
    visit = [s]
    que = [s]

    while que:
        tmp = que.pop(0)
        for i in graph[tmp]:
            if i not in visit:
                cnt[i] = cnt[tmp] + 1
                visit.append(i)
                que.append(i)
    
    return sum(cnt)

answer = []
for i in range(1, n+1):
    answer.append(bfs(i))

print(answer.index(min(answer))+1)