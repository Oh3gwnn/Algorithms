import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = reversed([int(input()) for _ in range(n)])
cnt = 0

for i in lst:
    cnt += k // i
    k %= i

print(cnt)