def solution(n):
    answer = []
    i = 2
    while(i<n+1):
        if n%i==0:
            if i not in answer: answer.append(i)
            n = int(n/i)
        else:
            i += 1
    return answer