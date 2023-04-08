#1 통과하는 코드 (효율성 시간 초과)
def solution(s):
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
    
#2 간단하게 적는다고 효율성이 올라가진 않는다. (효율성 시간 초과)
def solution(s):
    while '()' in s :
        s = s.replace("()", "")
    
    return s == ""

# 첫 번째 수정해서 통과
def solution(s):
    tmp = 0

    for a in s:
        if tmp < 0:
            break
        
        if a == '(':
            tmp += 1
        else:
            tmp -= 1
    
    return tmp == 0