import sys
input = sys.stdin.readline

t = int(input())
arr = [0] * 100
arr[0:4] = 1,1,1,2,2

for i in range(5, 100): arr[i] = arr[i-1] + arr[i-5]
for _ in range(t):
    n = int(input())
    print(arr[n-1])