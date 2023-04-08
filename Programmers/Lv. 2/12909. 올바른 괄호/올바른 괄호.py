# 일단 통과하는 코드 (효율성 시간 초과)
def solution(s):
    answer = True
    lst = [i for i in s]
    a = ''
    tmp = 0
        
    while lst != []:
        if tmp == 0:
            if lst[0] == ')' or lst[-1] == '(':
                return False
    
        a = lst.pop(0)
        if a == '(':
            tmp += 1
        else:
            tmp -= 1
    
    if tmp == 0 :
        return True
    else :
        return False