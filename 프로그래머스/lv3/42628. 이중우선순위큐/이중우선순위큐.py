import heapq

def solution(operations):
    answer = []
    
    for i in operations:
        tmp = i.split()
        
        if tmp[0] == "I" : 
            heapq.heappush(answer, int(tmp[1]))
            
        elif tmp[0] == "D" :
            # 런타임 에러의 이유 - 가장 위에있어야 했다.
            if len(answer) == 0: pass
        
            elif tmp[1] == "1":
                answer = heapq.nlargest(len(answer), answer)[1:]
                heapq.heapify(answer)
                
            else: heapq.heappop(answer)
                
    if not answer : return [0, 0]
    else : return [max(answer), min(answer)]