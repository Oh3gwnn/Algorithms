import sys
input = sys.stdin.readline

lst = []
for i in range(10):
    lst.append(int(input()) % 42)
print(len(set(lst)))