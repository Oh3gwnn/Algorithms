def solution(s):
    ans, cnt = 0, 0
    
    while (s != "1"):
        for i in s: 
            if i == "0": cnt += 1
        s = "".join(bin(int(len(s.replace("0", "")))))[2:]
        ans += 1
            
    return [ans, cnt]