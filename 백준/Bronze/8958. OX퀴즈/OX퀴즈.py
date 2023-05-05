import sys
input = sys.stdin.readline

n = int(input().rstrip())
result = [0]*n

for i in range(n):
    plus = 0
    ox = map(str, input())
    for s in ox:
        if s == "O":
            plus += 1
            result[i] += plus
        else :
            plus = 0


for i in range(n): print(result[i])