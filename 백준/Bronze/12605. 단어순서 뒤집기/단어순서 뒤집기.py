import sys
input = sys.stdin.readline

n = int(input())
lst = []
strlst = []

for x in range(n):
    lst = input().split()
    strlst.append("Case #" + str(x+1) + ": " + " ".join([i for i in reversed(lst)]))

for i in strlst:
    print(i)