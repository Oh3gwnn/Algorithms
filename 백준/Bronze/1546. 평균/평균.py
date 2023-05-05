import sys
input = sys.stdin.readline

n = map(int, input())
a = sorted(list(map(int, input().split())), reverse=True)

maxgrade = a[0]

for i in range(0, len(a)):
    a[i] = a[i]/maxgrade*100

print(sum(a)/len(a))