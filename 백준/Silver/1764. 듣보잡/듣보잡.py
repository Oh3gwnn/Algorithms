import sys
input = sys.stdin.readline

n, m = map(int, input().split())
know = [input().rstrip() for _ in range(n)]
unknow = [input().rstrip() for _ in range(m)]
ans = set(know+unknow)

dic = dict()
for i in (know + unknow):
    if i not in dic: dic[i] = 1
    else : dic[i] += 1

lst = [i[0] for i in sorted(dic.items(), key=lambda x : (-x[1], x[0]))[:n+m - len(ans)]]

print(n+m - len(ans))
for i in lst: print(i)