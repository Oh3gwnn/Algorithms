def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        print(s, e, k)
        tmp = 0
        for i in range(s, e+1):
            if k < arr[i]:
                if tmp == 0 or arr[i] < tmp: tmp = arr[i]
            
        if tmp == 0: answer.append(-1)
        else: answer.append(tmp)
                
    return answer