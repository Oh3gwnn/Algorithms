import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n): lst.append(int(input()))

dp = [1, 2, 4]
for i in range(3, max(lst)): dp.append(sum(dp[i-3:i]))

for i in lst: print(dp[i-1])