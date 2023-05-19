# 왜 리스트, 딕셔너리 하나 이렇게하면 시간초과 뜨고
# 딕셔너리 두개로 분리하면 시간초과가 안뜰까? 난잘몰

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

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# pk_list = [str(input().rstrip()) for _ in range(n)]

# for _ in range(m):
#     tmp = input().rstrip()
#     if tmp.isdigit(): print(pk_list[int(tmp)])
#     else: print(pk_list.index(tmp)+1)
