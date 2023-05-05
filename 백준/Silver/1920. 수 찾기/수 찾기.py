import sys
input = sys.stdin.readline

n = int(input())
A = set(map(int, input().split())) # list 사용 시 시간초과
m = int(input())
B = list(map(int, input().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)