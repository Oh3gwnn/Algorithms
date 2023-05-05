import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

print(min(s), max(s))