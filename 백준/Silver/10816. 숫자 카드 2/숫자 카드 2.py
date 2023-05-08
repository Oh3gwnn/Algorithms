import sys
input = sys.stdin.readline

n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))
answer = {}

for i in lst1:
    if i in answer: answer[i] +=  1
    else: answer[i] = 1

for i in lst2:
    if i in answer: print(answer[i], end=" ")
    else: print(0, end=" ")