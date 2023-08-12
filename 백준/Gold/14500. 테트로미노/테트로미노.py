import sys
input = sys.stdin.readline

def dfs(x, y, step, total):
    global answer
    if total + max_val*(4-step) <= answer: return
    if step == 4:
        answer = max(answer, total)
        return

    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if step == 2:
                visited[nx][ny] = True
                dfs(x, y, step+1, total+board[nx][ny])
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, step+1, total+board[nx][ny])
            visited[nx][ny] = False

if __name__ == "__main__": # global 변수 -> 인터프리터 직접 실행 시 작동
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_val = max(map(max, board))
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * M for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, 1, board[i][j])
            visited[i][j] = False
            
    print(answer)