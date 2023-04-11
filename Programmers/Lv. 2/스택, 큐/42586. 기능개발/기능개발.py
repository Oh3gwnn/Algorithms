def solution(progresses, speeds):
    answer = []
    result = []
    
    for i, s in enumerate(speeds):
        num = 0
        while progresses[i] < 100:
            progresses[i] += s
            num += 1
        result.append(num)
    
    print(result)
    num = 1
    tmp = result.pop(0)
    for i in result:
        if tmp >= i:
            num += 1
        else:
            if i > tmp:
                tmp = i
            answer.append(num)
            num = 1
            
    answer.append(num)        
    return answer