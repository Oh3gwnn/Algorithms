import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().split())
graph = list([] for _ in range(d+1))
for i in range(d): graph[i].append((i+1, 1))
distance = [INF] * (d+1)

for _ in range(n):
    idx, arrive, dist = map(int, input().split())
    if arrive <= d: graph[idx].append((arrive, dist))

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0

    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist: continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

dijkstra(0)
print(distance[d])