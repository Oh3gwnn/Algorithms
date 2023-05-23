import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
rs = [0, 0]

def solution(x, y, n):
    color = lst[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != lst[i][j]:
                solution(x, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                return
            
    if color == 0: rs[0] += 1
    else: rs[1] += 1

solution(0,0,n)
print(rs[0])
print(rs[1])