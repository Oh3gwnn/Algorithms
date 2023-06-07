import sys
input = sys.stdin.readline

n, m = map(int, input().split())
know_list = set(map(int, input().split()[1:]))
party = []

for _ in range(m): party.append(set(map(int, input().split()[1:])))


for _ in range(m):
    for people in party:
        if people & know_list:
            know_list = know_list.union(people)

ans = 0
for people in party:
    if people & know_list:
        continue
    else: ans += 1

print(ans)