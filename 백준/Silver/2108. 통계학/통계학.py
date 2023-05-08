import sys
input = sys.stdin.readline

def cb(lst):
    dic = {}
    for i in lst:
        if i in dic: dic[i] += 1
        else: dic[i] = 1
    dic = sorted(dic.items(), key= lambda x : (-x[1], x[0]))
    if dic[0][1] == dic[1][1]: print(dic[1][0])
    else: print(dic[0][0])


n = int(input())
lst = []
for i in range(n): lst.append(int(input().rstrip()))
if len(lst) > 1:
    print(int(round(sum(lst)/n, 0)))
    print(sorted(lst)[(n//2)])
    cb(lst)
    print(max(lst)-min(lst))
else:
    print(lst[0])
    print(lst[0])
    print(lst[0])
    print(0)