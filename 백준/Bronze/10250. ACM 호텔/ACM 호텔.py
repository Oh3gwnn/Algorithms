import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    h, w, n = map(int, input().split())
    last = n // h + 1
    first = n % h
    if n % h == 0:
        last = n // h
        first = h
    print(f"{first*100+last}")