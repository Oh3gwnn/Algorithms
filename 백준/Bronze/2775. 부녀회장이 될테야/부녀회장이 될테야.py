import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t): 
    k = int(input())
    n = int(input())
    zero = [z for z in range(1, n+1)]
    
    for i in range(k):
        for j in range(1, n):
            zero[j] += zero[j-1]
    
    print(zero[-1])