def solution(clothes):
    answer = 1
    today = {}
    
    for box in clothes:
        if box[1] in today:
            today[box[1]].append(box[0])
        else:
            today[box[1]] = [box[0]]
        
    for i in today.keys():
        answer *= (len(today[i]) + 1)
        
    return answer - 1