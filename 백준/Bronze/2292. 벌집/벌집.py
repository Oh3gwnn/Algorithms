# 이건 조금 생각했다. 어렵네
import sys
input = sys.stdin.readline

n = int(input())

start = 1
cnt = 1
while n > start:
    start += 6 * cnt
    cnt += 1

print(cnt)