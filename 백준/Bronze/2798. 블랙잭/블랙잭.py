from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
combi = list(combinations(nums, 3))
answer = 0

for i in combi:
    if answer < sum(i) <= m:
        answer = sum(i)

print(answer)