import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = list([] for _ in range(n+1))

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dij(s):
    q = []
    D = [INF] * (n+1)

    heapq.heappush(q, (0, s))
    D[s] = 0

    while q:
        dist, now = heapq.heappop(q)
        if D[now] < dist: continue

        for next, cost in graph[now]:
            if D[next] > (dist + cost): 
                D[next] = (dist + cost)
                heapq.heappush(q, ((dist + cost), next))

    return D

res = 0
for i in range(1, n+1):
    wnt = dij(i)
    bak = dij(x)
    res = max(res, wnt[x] + bak[i])

print(res)