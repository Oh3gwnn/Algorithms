import sys
input = sys.stdin.readline

n = int(input())

lst = [list(map(int, input().rstrip())) for _ in range(n)]

def solution(x, y, n):
    tmp = lst[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if tmp != lst[i][j]:
                print("(", end="")
                n = n//2
                solution(x, y, n)
                solution(x, y+n, n)
                solution(x+n, y, n)
                solution(x+n, y+n, n)
                print(")", end="")
                return
    else:
        if tmp == 1: print("1", end="")
        else: print("0", end="")
        return

solution(0, 0, n)