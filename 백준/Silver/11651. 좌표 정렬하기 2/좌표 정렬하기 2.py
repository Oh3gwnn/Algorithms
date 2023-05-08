import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n): 
    x, y = map(int, input().split())
    lst.append((x, y))

for i, j in sorted(lst, key=lambda x : (x[1], x[0])): print(i, j)