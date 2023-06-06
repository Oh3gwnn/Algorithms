import sys
input = sys.stdin.readline

n = int(input())

def round1(num):
    return int(num) + (1 if (num - int(num) >= 0.5) else 0)

if n:
    lst = [int(input()) for _ in range(n)]
    a = round1(n * 0.15)
    lst = sorted(lst)[a:n-a]
    print(round1(sum(lst)/len(lst)))
else:
    print(0)