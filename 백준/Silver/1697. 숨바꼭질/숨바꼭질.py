from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
v = [0] * (10 ** 5 + 1)

q = deque()
q.append(n)

while q:
    tmp = q.popleft()
    if tmp == k:
        print(v[tmp])
        break
    
    for i in (tmp-1, tmp+1, tmp*2):
        if (0 <= i <= 10 ** 5) and (v[i] == 0):
            v[i] = v[tmp] + 1
            q.append(i)
