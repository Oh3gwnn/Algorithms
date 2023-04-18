# bfs 틀은 짰는데, 재귀함수로 들어가게는 안했었다.(9/13점)
# 그니까 dfs도 그렇고 재귀로 들어가는 연습을 해야겠다.
# 반제는 좀 궁금하긴한데, 아무도 안 적어놨다.
# 아마 한번 돌아가고 말아버리니까 놓치는 노드가 있지 않았을까 싶다.

# 아하 반제 생각하다가 문득 생각났는데
# 11, 11 이런식으로 따로따로 연결되어있는 네트워크를 못 센 것 같다.

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def bfs(start, visited, computers):
        visited[start] = 1
        que = [start]
        while que:
            q = que.pop(0)

            for i in range(n):
                if computers[q][i] == 1 and not visited[i]:
                    visited[i] = 1
                    que.append(i)
                    
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers)
            answer += 1
                
    return answer