import sys
input = sys.stdin.readline

test = int(input())
for i in range(test):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    que = [(x, i) for i, x in enumerate(lst)]
    cnt = 0
    
    while True:
        if que[0][0] == max(que)[0]:
            tmp = que.pop(0)
            cnt += 1
            if tmp[1] == m: break
        else:
            que.append(que.pop(0))
    
    print(cnt)