import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    num = sum(map(int, str(i)))
    nsum = i + num

    if nsum == n:
        print(i)
        break
    if i == n:
        print(0)