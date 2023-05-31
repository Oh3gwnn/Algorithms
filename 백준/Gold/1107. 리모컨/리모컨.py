import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

lst = list(map(int, input().split()))

cnt = abs(100 - n)

for i in range(1000001):
    i = str(i)

    for j in range(len(i)):
        if int(i[j]) in lst:
            break

        elif j == len(i) - 1:
            cnt = min(cnt, abs(int(i) - n) + len(i))

print(cnt)