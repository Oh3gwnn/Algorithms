# BFS(너비 우선 탐색)
def solution(numbers, target):
    leaves = [0]
    answer = 0
    
    for num in numbers:
        temp = []
        
        for leaf in leaves:
            temp.append(leaf + num)
            temp.append(leaf - num)
        
        leaves = temp
        
    for leaf in leaves:
        if leaf == target:
            answer += 1
            
    return answer