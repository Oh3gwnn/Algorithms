import sys
input = sys.stdin.readline

n = int(input()) 
queue = []

for i in range(n):
    tmp = input().rstrip()

    if "push" in tmp:
        queue.append(int(tmp[5:]))

    elif tmp == "pop":
        print(queue.pop(0)) if queue else print(-1)
        
    elif tmp == "size":
        print(len(queue))

    elif tmp == "empty":
        print(0) if queue else print(1)

    elif tmp == "front": 
        print(queue[0]) if queue else print(-1)

    elif tmp == "back": 
        print(queue[-1]) if queue else print(-1)