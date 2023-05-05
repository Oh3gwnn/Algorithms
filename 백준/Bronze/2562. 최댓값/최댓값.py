lst = [0]*9
for i in range(0, 9): lst[i] = int(input())

for i, x in enumerate(lst):
    lst[i] = (x, i+1)

print(max(lst)[0])
print(max(lst)[1])