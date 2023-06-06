import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
S = input()

s = "I" + "OI" * n

cnt = 0
for i in range(m):
    if s == S[i:i+len(s)]:
        cnt += 1

print(cnt)