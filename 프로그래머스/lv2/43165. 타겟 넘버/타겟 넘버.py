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

# DFS (깊이 우선 탐색)
'''
answer = 0

def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer
'''