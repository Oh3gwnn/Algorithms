import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

def zfilp(n, r, c):
    if n == 0: return 0
    return 2 * (r % 2) + (c % 2) + 4 * zfilp(n-1, int(r/2), int(c/2))

print(zfilp(n, r, c))