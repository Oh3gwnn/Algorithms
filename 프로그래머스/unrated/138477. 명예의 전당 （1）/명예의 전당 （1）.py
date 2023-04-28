def solution(k, score):
    answer = []
    stack = []*len(score)
    
    for i in range(len(score)):
        if len(stack) != k : 
            stack.append(score[i])
            stack.sort()
            answer.append(stack[0])
            
        elif (len(stack) == k):
            if score[i] > min(stack):
                stack.pop(0)
                stack.append(score[i])
                stack.sort()
                answer.append(stack[0])
            else : answer.append(stack[0])
            
    return answer