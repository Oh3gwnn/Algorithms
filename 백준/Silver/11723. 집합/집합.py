import sys
input = sys.stdin.readline

s = int(input())
set_list = set()
tmp = list()
for _ in range(s):
    tmp = input().split()
    
    if tmp[0] == "add":
        if int(tmp[1]) not in set_list: set_list.add(int(tmp[1]))
    elif tmp[0] == "remove":
        if int(tmp[1]) in set_list: set_list.remove(int(tmp[1]))
    elif tmp[0] == "check":
        if int(tmp[1]) in set_list: print(1)
        else: print(0)
    elif tmp[0] == "toggle":
        if int(tmp[1]) in set_list: set_list.remove(int(tmp[1]))
        else: set_list.add(int(tmp[1]))
    elif tmp[0] == "all":
        set_list = set(range(1, 21))
    elif tmp[0] == "empty":
        set_list = set()