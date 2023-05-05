import sys
input = sys.stdin.readline

n = int(input())
devil = 666

while n:
    if "666" in str(devil): n -= 1
    devil += 1

print(devil - 1)