import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = list([] for _ in range(n+1))
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1)) # 거리가 무조건 1칸

def dijkstra(start):    # 특정한 도시 x에서 시작
    distance[start] = 0 # 거리는 0부터
    queue = list()      # BFS 구조랑 비슷

    # queue에 (dist, now) 저장
    # 
    heapq.heappush(queue, (0, start)) 

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist: continue

        for i in graph[now]:
            # cost는 i[1]을 더한다.(다익스트라 기준)
            # 이 문제에서는 +1 해준다는 느낌으로 하면 될 것 같음
            cost = dist + i[1] 
            # distance[i]라고 했을 때 i == start를 제외하고는 INF
            # 즉, 아직 가본 적 없는 도시니까 진행하는 조건문
            if cost < distance[i[0]]:
                distance[i[0]] = cost # 그래서 현재 거리를 넣는 것
                # 지금까지의 거리와 현재 위치(도시)를 push
                heapq.heappush(queue, (cost, i[0])) 

dijkstra(x)

ans = list()
[ans.append(i) for i in range(1, n+1) if distance[i] == k]

if len(ans) == 0: print(-1)
else: [print(i, end='\n') for i in ans]