import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = list([] for _ in range(n+1))
distance = [INF] * (n+1)
for _ in range(m):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))

def dijkstra(start):
    q = list()
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

s, e = map(int, input().split())
dijkstra(s)
print(distance[e])