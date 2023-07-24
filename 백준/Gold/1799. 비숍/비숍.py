import sys
input = sys.stdin.readline

white_points = []  # 하얀 비숍들이 들어갈 수 있는 칸
black_points = []  # 검은 비숍들이 들어갈 수 있는 칸
white_max = [0]  # 하얀색 칸에 놓을 수 있는 비숍의 최대 개수
black_max = [0]  # 검은색 칸에 놓을 수 있는 비숍의 최대 개수

size = int(input())

for i in range(size):
    board = list(map(int, input().split()))
    for j in range(size):
        if board[j] == 1:
            if (i + j) % 2 == 0:
                white_points.append([i, j])
            else:
                black_points.append([i, j])

def dfs(next_index, selected, points, max_count):
    if next_index == len(points):
        count = sum(selected)
        max_count[0] = max(max_count[0], count)
    else:
        selected[next_index] = True
        if check(next_index, selected, points):
            dfs(next_index + 1, selected, points, max_count)
        selected[next_index] = False
        dfs(next_index + 1, selected, points, max_count)

def check(next_index, selected, points):
    point = points[next_index]
    for i in range(next_index):
        if (
            selected[i]
            and abs(points[i][0] - point[0])
            == abs(points[i][1] - point[1])
        ):
            return False
    return True

dfs(0, [False] * len(white_points), white_points, white_max)
dfs(0, [False] * len(black_points), black_points, black_max)

print(white_max[0] + black_max[0])