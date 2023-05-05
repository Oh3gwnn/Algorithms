import sys
input = sys.stdin.readline

n = int(input())
stack, res = [], []
tmp, flg = 1, 0

for i in range(n):
    num = int(input())
    while tmp <= num:
        stack.append(tmp)
        res.append("+")
        tmp += 1
    
    if stack[-1] == num:
        stack.pop()
        res.append("-")
    else:
        print("NO")
        flg = 1
        break

if flg == 0:
    for i in res: print(i)