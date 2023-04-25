def solution(s):
    tmp = []
    for i in s:
        if not tmp : tmp.append(i)
        elif tmp[-1] == i: tmp.pop()
        else : tmp.append(i)
    return 1 if not tmp else 0