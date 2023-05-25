import sys
input = sys.stdin.readline

n = int(input())
ans = [0, 1, 2, 3, 5]
for i in range(5, 1001): ans.append(ans[i-2] + ans[i-1])
print(ans[n] % 10007)