import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

a = w-x if w-x < x else x
b = h-y if h-y < y else y
print(a if a<b else b)