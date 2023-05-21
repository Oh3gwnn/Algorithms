import sys
input = sys.stdin.readline

n = int(input())
paper = [[i for i in map(int, input().split())] for _ in range(n)]
use_dict = {-1:0, 0:0, 1:0}

def equalpaper(row, col, n):
    tmp = paper[row][col]
    for i in range(row, row+n):
        for j in range(col, col+n):
            if tmp != paper[i][j]:
                for x in range(3):
                    for y in range(3):
                        equalpaper(row+x*n//3, col+y*n//3, n//3)
                return
            
    use_dict[tmp] += 1

equalpaper(0,0,n)
print(use_dict[-1],use_dict[0],use_dict[1])