n = int(input())
s = int(input())
res = 0
for i in range(n-1, -1, -1):
    res += s // 10**i
    s = s % 10**i
    
print(res)