import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]

dp = []

if len(lst) <= 2: print(sum(lst))
else:
    dp.append(lst[0])
    dp.append(lst[0]+lst[1])
    dp.append(max(lst[0]+lst[2], lst[1]+lst[2]))

    for i in range(3, n):
        dp.append(max(dp[i-2] + lst[i], dp[i-3] + lst[i] + lst[i-1]))

    print(dp[-1])