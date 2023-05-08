import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    tmp = (str(input().rstrip()))
    if len(tmp) % 2 == 1: 
        print("NO")
        continue
    else:
        while True:
            if "()" in tmp:
                tmp = tmp.replace("()", "")
            else: break

    if not tmp: print("YES")
    else: print("NO")