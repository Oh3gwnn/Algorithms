import sys
input = sys.stdin.readline

# 1차원배열과 min, max로 범위 축소한 풀이 464ms(얘도 pypy3로 안하면 시간초과)
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
lst = []
for i in range(n): lst += list(map(int, input().split()))

anstime = sys.maxsize
ans = lst[0]
blocks = sum(lst)

for t in range(max(lst), min(lst)-1, -1):
    if blocks + b >= t * n * m:
        time = 0

        for i in lst:
            tmp = i - t
            if tmp > 0:
                time += tmp * 2
            elif tmp < 0:
                time -= tmp * 1
        
        if time < anstime:
            anstime = time
            ans = t

print(anstime, ans)

# 브루스포스 풀이(시간초과 -> pypy3로 변경 -> 통과) 816ms
# n, m, b = map(int, input().split())
# lst = [list(map(int, input().split())) for _ in range(n)]
# ans = sys.maxsize
# idx = 0

# for g in range(min(min(lst)), max(max(lst))+1):
#     maxg, ming = 0, 0

#     for i in range(n):
#         for j in range(m):
#             if lst[i][j] >= g:
#                 maxg += lst[i][j] - g

#             else: ming += g - lst[i][j]
    
#     if maxg + b >= ming:
#         if ming + (maxg * 2) <= ans:
#             ans = ming + (maxg * 2)
#             idx = g

# print(ans, idx)