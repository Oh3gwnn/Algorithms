import sys
input = sys.stdin.readline
a, b = map(str, input().split())
a = int(a[-1::-1])
b = int(b[-1::-1])
print(a if a>b else b)