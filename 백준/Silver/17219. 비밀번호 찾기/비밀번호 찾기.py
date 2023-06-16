import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
listdict = defaultdict(list)

for _ in range(n):
    net, pw = list(input().rstrip().split())
    listdict[net].append(pw)

for _ in range(m): print("".join(listdict[input().rstrip()]))