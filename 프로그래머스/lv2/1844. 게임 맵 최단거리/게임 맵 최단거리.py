# BFS와 que가 쓰였는데 빨리 배우는 게 좋을 것 같다.
# 레벨 2인데 손도 못대겠다.
def solution(maps):
    ax = [0, 0, -1, 1]
    ay = [-1, 1, 0, 0]
    que = [(0,0)]

    while que:
        x, y = que.pop(0)

        for i in range(4):
            mx = x + ax[i]
            my = y + ay[i]

            if mx < 0 or mx >= len(maps) or my < 0 or my >= len(maps[0]): continue

            if maps[mx][my] == 0: continue

            if maps[mx][my] == 1:
                maps[mx][my] = maps[x][y] + 1
                que.append((mx, my))
                
    answer = maps[-1][-1]
    return -1 if answer == 1 else answer