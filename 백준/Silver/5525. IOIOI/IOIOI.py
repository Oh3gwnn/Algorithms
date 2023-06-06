import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

s = "I" + "OI" * n
cnt = 0

S = str(input())

for i in range(m):
    if s == S[i:i+len(s)]:
        cnt += 1

print(cnt)