import sys
input = sys.stdin.readline

n = int(input())

lst = [1, 3, 5, 11]

for i in range(4, n): lst.append(lst[i-1] + 2 * lst[i-2])

print(lst[n-1]%10007)