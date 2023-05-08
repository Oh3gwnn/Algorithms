import sys
input = sys.stdin.readline

n = int(input())
s = []

for _ in range(n):
    s.append(int(input().rstrip()))

s = sorted(s)
for i in range(n):
    print(s[i])