def solution(l, r):
    answer = []
    start, end = 0, 0
    
    tmp = l
    while tmp > 1:  
        tmp //= 10
        start += 1
    
    tmp = r
    while tmp > 1: 
        tmp //= 10
        end += 1
                        
    for i in range(start, 2**end):
        tmp = 5*int(bin(i)[2:])
        if l <= tmp <= r:
            answer.append(tmp)
    
    if not answer : answer.append(-1)
    
    return answer