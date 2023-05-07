import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2

    tmp = 0
    for tree in trees:
        if tree >= mid:
            tmp += tree - mid
    
    if tmp >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# 정답은 맞는 것 같은데 시간 초과
# answer = 0
# for i in range(max(trees)-1, 0, -1):
#         res = [j - i for j in trees if j >= i]
#         if sum(res) >= m :
#             answer = i
#             break
# print(answer)