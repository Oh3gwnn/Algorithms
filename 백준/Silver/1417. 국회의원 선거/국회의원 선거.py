import sys
input = sys.stdin.readline

n, select = int(input()), int(input())
if n == 1:
    print(0)
    exit(0)

vote_list = [int(input()) for _ in range(n-1)]
vote_list.sort(reverse=True)

cnt = 0
while vote_list[0] >= select:
    select += 1
    vote_list[0] -= 1
    cnt += 1
    vote_list.sort(reverse=True)

print(cnt)