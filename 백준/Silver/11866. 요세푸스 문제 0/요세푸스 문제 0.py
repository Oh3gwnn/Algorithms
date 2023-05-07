import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = [i for i in range(1, n+1)]
answer = []

while lst:
    for i in range(k-1):
        lst.append(lst.pop(0))
    answer.append(lst.pop(0))

print("<" + ", ".join(str(i) for i in answer) + ">")
