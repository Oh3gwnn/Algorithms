import sys
input = sys.stdin.readline

lst = input().split('-')

a = sum(list(map(int, lst[0].split('+'))))

for i in lst[1:]:
    for j in i.split('+'):
        a -= int(j)

print(a)