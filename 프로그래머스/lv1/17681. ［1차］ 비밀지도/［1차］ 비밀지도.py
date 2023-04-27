def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        num = bin(arr1[i] | arr2[i])[2:].zfill(n)
        num = num.replace('0', ' ').replace('1', '#')
        answer.append(num)
    
    return answer