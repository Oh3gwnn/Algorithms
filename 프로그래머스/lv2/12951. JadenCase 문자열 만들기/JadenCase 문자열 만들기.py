def solution(s):
    
    answer = "".join([i.lower().capitalize() + " " for i in s.split(" ")])
    return answer[0:len(s)]