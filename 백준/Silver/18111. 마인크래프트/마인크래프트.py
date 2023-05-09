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