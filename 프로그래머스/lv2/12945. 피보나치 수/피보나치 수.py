def solution(n):
    answer = 0
    lst = [0] * (n+1)
    lst[1] = 1
    for i in range(0, n+1):
        if i+1 == n: break
        lst[i+2] = lst[i] + lst[i+1]
    return lst[-1]%1234567