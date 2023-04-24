def solution(n):
    n2 = n
    while 1:
        n2 += 1
        a = [i for i in bin(n) if i == '1']
        b = [i for i in bin(n2) if i == '1']
        if a == b:
            break
    return n2