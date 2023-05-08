import sys
input = sys.stdin.readline

l = int(input())
s = str(input())
ans = 0

for i in range(l):
    ans += (ord(s[i]) - 96) * (31 ** i)

print(ans % 1234567891)