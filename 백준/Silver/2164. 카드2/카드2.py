# 로직은 맞는데 시간초과 --> deque 사용..

import sys
from collections import deque as dq

input = sys.stdin.readline

n = int(input())
que = dq(range(1, n+1))

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que[0])