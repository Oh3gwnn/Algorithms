import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n): 
    lst.append(str(input().rstrip()))

lst = sorted(set(lst), key = lambda x : (len(x), x))

for i in lst: print(i)