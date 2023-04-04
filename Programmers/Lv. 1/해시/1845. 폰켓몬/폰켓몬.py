def solution(nums):    
    answer = len(set(nums))
    select = len(nums)/2
    return answer if answer < select else select