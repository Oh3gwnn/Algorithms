# 메모리 초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# lst = list()

# for i in range(n):
#     x = int(input())
#     lst.append(x)

# [print(i) for i in sorted(lst)]

import sys
input = sys.stdin.readline

n = int(input())
lst = [0] * 10001

for i in range(n):
    x = int(input())
    lst[x] += 1

for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)