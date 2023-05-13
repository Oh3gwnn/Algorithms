import sys
input = sys.stdin.readline

n = int(input())

lst = sorted(list(map(int, input().split())))
time = 0

for i in range(1, n+1): time += sum(lst[:i])
    
print(time)