import sys
from itertools import combinations
from collections import defaultdict
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    res = 999999
    n = int(input())
    mbti = list(map(str, input().split()))
    m = defaultdict(int)
    for i in mbti: m[i] += 1
    for i in m:
        if m[i] >= 3:
            print(0)
            break
    else:
        for i in combinations(mbti, 3):
            a, b, c = i[0], i[1], i[2]
            cnt = 0
            for j in range(4):
                c1 = 1 if a[j] != b[j] else 0
                c2 = 1 if b[j] != c[j] else 0
                c3 = 1 if a[j] != c[j] else 0
                cnt += c1 + c2 + c3
            res = min(res, cnt)
        print(res)