def solution(s):
    ans = 0
    cnt = 0
    
    while (s != "1"):
        for i in s: 
            if i == "0":
                cnt += 1
        s = "".join(bin(int(len(s.replace("0", ""))))).replace("0b", "")
        ans += 1
            
    return [ans, cnt]