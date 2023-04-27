# 스택으로 풀다가 안풀려서 다르게 풀었다...
# 브론즈..구나...

import sys
input = sys.stdin.readline

n = int(input())
stack = []
cnt = 0
max = 0

for i in range(0, n):
    stack.append(int(input()))

for i in reversed(stack):
    if max < i:
        max = i
        cnt += 1

print(cnt)