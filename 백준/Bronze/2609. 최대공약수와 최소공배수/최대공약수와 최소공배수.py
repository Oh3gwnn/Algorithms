# import math
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

# 유클리드 호제법
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))

# print(math.gcd(a, b)) 최대공약수
# print(math.lcm(a, b)) 최소공배수