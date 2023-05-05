import sys
input = sys.stdin.readline

def Primes(num):
    if num == 2: print(2)
    elif num >= 3:
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                num = 1
                break
        if num != 1:
            print(num)

m, n = map(int, input().split())

for i in range(m, n+1):
    Primes(i)