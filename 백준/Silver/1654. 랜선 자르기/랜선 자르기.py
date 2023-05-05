import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]

start, end = 1, int(sum(lst)/n)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lst:
        cnt += i // mid
    
    if cnt >= n: start = mid + 1
    else: end = mid - 1

print(end)