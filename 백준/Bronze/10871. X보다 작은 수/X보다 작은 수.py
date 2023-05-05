n, x = map(int, input().split())
a = list(map(int, input().split()))

res = []
for i in range(n):
    if a[i] < x: res.append(a[i])

print(" ".join(str(i) for i in res))