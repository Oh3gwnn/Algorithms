from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 0
    
    while queue:
        v = queue.popleft()
        cnt += 1
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
    return cnt

def solution(n, wires):
    answer = n - 2
    
    for i in range(len(wires)):
        tmps = wires.copy()
        graph = [[] for i in range(n+1)]
        visited = [False] * (n+1)
        tmps.pop(i)
        
        for wire in tmps:
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)
            
        for idx,g in enumerate(graph):
            if g != []:
                start = idx
                break
                
        cnts = bfs(graph, start, visited)
        other_cnts = n - cnts
        
        if abs(cnts - other_cnts) < answer:
            answer = abs(cnts - other_cnts)
            
    return answer