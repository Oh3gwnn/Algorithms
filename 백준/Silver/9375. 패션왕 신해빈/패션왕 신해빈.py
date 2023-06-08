import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    fashion = dict()
    n = int(input())

    for _ in range(n):
        a, b = input().rstrip().split()
        if b not in fashion : fashion[b] = 1
        else : fashion[b] += 1

    ans = 1
    for i in fashion : ans *= (fashion[i]+1)
    print(ans-1)