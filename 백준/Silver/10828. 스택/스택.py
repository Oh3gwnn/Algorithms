import sys
input = sys.stdin.readline

n = int(input()) 
stack = []

for i in range(n):
    tmp = input().rstrip() # 아하! 개행문자 제거

    if "push" in tmp:
        stack.append(int(tmp[5:]))

    elif tmp == "pop":
        print(stack.pop()) if stack else print(-1)
        
    elif tmp == "size":
        print(len(stack))

    elif tmp == "empty":
        print(0) if stack else print(1)

    elif tmp == "top": 
        print(stack[-1]) if stack else print(-1)