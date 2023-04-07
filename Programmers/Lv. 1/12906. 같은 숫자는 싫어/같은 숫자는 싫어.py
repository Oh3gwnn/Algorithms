def solution(arr):
    answer = []
    top = -1
    for i in arr:
        if i != top:
            top = i
            answer.append(i)

    return answer