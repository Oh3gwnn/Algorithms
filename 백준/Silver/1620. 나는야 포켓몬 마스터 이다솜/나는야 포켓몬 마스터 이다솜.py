import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pk_num, pk_name = dict(), dict()
for i in range(1, n+1):
    pk = input().rstrip()
    pk_num[i] = pk
    pk_name[pk] = i

for _ in range(m):
    tmp = input().rstrip()
    if tmp.isdigit(): print(pk_num[int(tmp)])
    else: print(pk_name[tmp])