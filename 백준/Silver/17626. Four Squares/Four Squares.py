import sys, math
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    cnt = 50_000
    for j in range(1, int(math.sqrt(i))+ 1):
        cnt = min(cnt, dp[i - j**2])
    dp.append(cnt+1)

print(dp[n])