def solution(n,a,b):
    answer = 0
    lst = list(range(1, n+1))
    rnd = 0
    
    while (n>1):
        tmp = []
        n //= 2
        
        for i in range(n):
            if isinstance(lst[2*i], int):
                tmp.append([lst[2*i], lst[2*i+1]])
            else : tmp.append(lst[2*i] + lst[2*i+1])
        rnd += 1
        
        for i in range(len(tmp)):
            if (a in tmp[i]) & (b in tmp[i]):
                return rnd
            
        lst = tmp