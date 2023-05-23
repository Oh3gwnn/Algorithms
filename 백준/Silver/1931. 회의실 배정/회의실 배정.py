import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n): lst.append(list(map(int, input().split())))

lst = sorted(lst, key=lambda x: x[0])
lst = sorted(lst, key=lambda x: x[1])

tmp, cnt = 0, 0
for s, e in lst:
    if s >= tmp:
        cnt += 1
        tmp = e

print(cnt)