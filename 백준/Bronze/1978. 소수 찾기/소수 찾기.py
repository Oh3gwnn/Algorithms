import sys
input = sys.stdin.readline

n = int(input())
primes = map(int, input().split())
ans = 0

for i in primes:
    cnt = 0
    
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
        
        if cnt == 0:
            ans += 1

print(ans)