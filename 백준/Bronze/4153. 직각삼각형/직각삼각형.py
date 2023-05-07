import sys
input = sys.stdin.readline

while 1:
    n = list(map(int, input().split()))
    if n == [0, 0, 0]: break

    maxn = max(n)
    n.remove(maxn)
    
    if n[0]**2 + n[1]**2 == maxn**2: print("right")
    else : print("wrong")