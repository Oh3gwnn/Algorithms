# "BW...", "WB..." 문자열 2개랑 비교해서 풀어봤는데
# 더 간단하게 구현.
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
org, cnt = [], []

for _ in range(n): org.append(input())

for i in range(n-7):
    for j in range(m-7):
        idx1, idx2 = 0, 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if org[a][b] != "W": idx1 += 1
                    if org[a][b] != "B": idx2 += 1
                else:
                    if org[a][b] != "B": idx1 += 1
                    if org[a][b] != "W": idx2 += 1
        cnt.append(min(idx1, idx2))
print(min(cnt))