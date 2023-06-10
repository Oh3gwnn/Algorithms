import sys
input = sys.stdin.readline

m, n = map(int, input().split())
lst = list(map(int, input().split()))
lstsum = [0]
tmp = 0   

for i in lst:
    tmp += i
    lstsum.append(tmp)
 
for i in range(n):
    a, b = map(int, input().split())
    print(lstsum[b] - lstsum[a-1])
