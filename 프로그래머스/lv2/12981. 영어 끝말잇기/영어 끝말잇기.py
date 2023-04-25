def solution(n, words):
    cnt = 0
    answer = []
    lst = []

    for i in words:
        if len(lst) % n == 0:
            cnt += 1
        if not lst : lst.append(i)
        elif (lst[-1][-1] == i[0]) & (i not in lst) : lst.append(i)
        else : 
            return [(len(lst)+1)%n if (len(lst)+1)%n!=0 else n, cnt]
        
    return [0, 0]