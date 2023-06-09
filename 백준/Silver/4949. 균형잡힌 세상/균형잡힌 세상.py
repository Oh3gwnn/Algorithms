import sys
input = sys.stdin.readline

while 1:
    s = str(input().rstrip())
    stack = []
    if s == ".": break
    
    for i in s:
        if i == "[" or i == "(": stack.append(i)
        elif i == "]": 
            if len(stack) != 0 and stack[-1] == "[": stack.pop()
            else: 
                stack.append(i)
                break
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(": stack.pop()
            else: 
                stack.append(i)
                break

    if not stack: print("yes")
    else: print("no")