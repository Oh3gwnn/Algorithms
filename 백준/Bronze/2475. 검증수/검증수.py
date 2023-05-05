lst = list(map(int, input().split()))

for i in range(0, len(lst)):
    lst[i] = lst[i]**2

print(sum(lst)%10)