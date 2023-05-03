import sys
input = sys.stdin.readline

n = int(input())
coordinate = list(map(int, input().split()))
dim = []
cnt = 0

for i, d in enumerate(coordinate): dim.append([d, i])
dim.sort()
tmp = dim[0][0]

for i in range(len(dim)):
    if tmp == dim[i][0]: dim[i][0] = cnt
    elif tmp < dim[i][0]:
        cnt += 1
        tmp = dim[i][0]
        dim[i][0] = cnt
        
dim.sort(key=lambda x : x[1])

print(" ".join(str(i[0]) for i in dim))