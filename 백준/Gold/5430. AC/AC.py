import sys
input = sys.stdin.readline
from collections import deque
t = int(input())

for _ in range(t):
    tmp, flag = 0, 0
    p = input().rstrip()
    n = int(input())
    xlist = deque(input().rstrip()[1:-1].split(','))
    if n == 0: xlist = []
    
    for i in p:
        if i == 'R': tmp += 1
        elif i == 'D':
            if not xlist:
                print("error")
                flag = 1
                break
            if tmp % 2 == 0: xlist.popleft()
            else : xlist.pop()

    if flag == 0:
        if tmp%2==0 : 
            print("["+ ",".join(xlist) +"]")
        else :
            xlist.reverse()
            print("["+ ",".join(xlist) +"]")