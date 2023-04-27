def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        num = bin(arr1[i] | arr2[i])[2:].zfill(n) # rjust(n, "0")도 된다. zfill()보다 더 범용적(?)이다.
        num = num.replace('0', ' ').replace('1', '#')
        answer.append(num)
    
    return answer