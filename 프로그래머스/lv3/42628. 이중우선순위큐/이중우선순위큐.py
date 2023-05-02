import heapq

def solution(operations):
    answer = []
    
    for i in operations:
        if i[0] == "I" : 
            heapq.heappush(answer, int(i[2:]))
            
        else:
            if len(answer) == 0: pass
        
            elif i[2] == "-":
                heapq.heappop(answer)
            else:
                answer = heapq.nlargest(len(answer), answer)[1:]
                heapq.heapify(answer)
                    
    if not answer : return [0, 0]
    else : return [max(answer), min(answer)]