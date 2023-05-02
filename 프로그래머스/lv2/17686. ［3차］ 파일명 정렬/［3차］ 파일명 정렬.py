def solution(files):
    answer = []
    head, number, tail = '', '', ''
    
    for f in files:
        for i in range(len(f)):
            if f[i].isdigit():
                head = f[:i]
                number = f[i:]
                
                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
        
                answer.append([head, number, tail])
                head, number, tail = '', '', ''
                break
                
    answer.sort(key = lambda x : (x[0].lower(), int(x[1])))
        
    return ["".join(i) for i in answer]