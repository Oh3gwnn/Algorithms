import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n): 
    x, y = map(int, input().split())
    lst.append((x, y))

for i, j in sorted(lst): print(i, j)