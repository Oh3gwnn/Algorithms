def solution(l, r):
    answer = []
    start, tmp = 1, 5
        
    while True :
        if tmp > r: break
        tmp = 5 * int(bin(start)[2:])
        if l <= tmp <= r:
            answer.append(tmp)
        start += 1
    
    return [-1] if not answer else answer