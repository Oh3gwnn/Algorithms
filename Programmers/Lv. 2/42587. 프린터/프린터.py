#1 정확도 17/20 (3개는 런타임에러)
'''
def solution(priorities, location):
    answer = 0
    lst = [(p, i) for i, p in enumerate(priorities)]
    
    while True:
        tmp = lst.pop(0)
        if tmp[0] < max(lst)[0]:
            lst.append(tmp)
        else:
            answer += 1
            print(lst)
            if tmp[1] == location:
                return answer
'''
        
#2 any() 참고해서 다시 품
def solution(priorities, location):
    answer = 0
    lst = [(p, i) for i, p in enumerate(priorities)]
    
    while True:
        tmp = lst.pop(0)
        if any(tmp[0] < l[0] for l in lst):
            lst.append(tmp)
        else:
            answer += 1
            print(lst)
            if tmp[1] == location:
                return answer