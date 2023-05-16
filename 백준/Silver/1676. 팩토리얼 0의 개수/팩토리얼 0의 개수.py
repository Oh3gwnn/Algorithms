from math import factorial
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for x in str(factorial(n))[::-1]:
    if x != '0':
        break
    cnt += 1
    
print(cnt)