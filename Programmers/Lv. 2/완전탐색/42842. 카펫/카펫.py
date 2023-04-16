def solution(brown, yellow):
    result = brown + yellow
    
    for i in range(1, result+1):
        if yellow % i == 0:
            x = yellow // i
            y = yellow//(yellow // i)
            
            if x >= y:
                browns_topbot = x+2
                browns_topbot *= 2
                browns_LR = 2*(y)
                
                if brown == (browns_topbot+browns_LR):
                    return [x+2, y+2]