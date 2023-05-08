import sys
input = sys.stdin.readline

n = int(input()) 
deque = []

for i in range(n):
    tmp = input().rstrip()

    if "push_front" in tmp:
        deque.insert(0, int(tmp[11:]))
    elif "push_back" in tmp:
        deque.append(int(tmp[10:]))

    elif tmp == "pop_front":
        print(deque.pop(0)) if deque else print(-1)
    elif tmp == "pop_back":
        print(deque.pop()) if deque else print(-1)
        
    elif tmp == "size":
        print(len(deque))

    elif tmp == "empty":
        print(0) if deque else print(1)

    elif tmp == "front": 
        print(deque[0]) if deque else print(-1)

    elif tmp == "back": 
        print(deque[-1]) if deque else print(-1)