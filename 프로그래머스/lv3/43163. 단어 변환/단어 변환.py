def solution(begin, target, words):
    answer = 0
    visited = [0] * len(words)
    q = []
    q.append([begin, 0])
    
    while q:
        wd, cnt = q.pop(0)
        if wd == target:
            answer = cnt
            break
            
        for i in words:
            tmp = 0
            if not visited[words.index(i)]:
                for j in range(len(i)):
                    if wd[j] != i[j]:
                        tmp += 1

                if tmp == 1:
                    q.append([i, cnt+1])
                    visited[words.index(i)] = 1
                    
    return answer