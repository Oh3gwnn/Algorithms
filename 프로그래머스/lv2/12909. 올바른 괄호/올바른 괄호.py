# 아마 처음에 '()'를 반복문으로 replace() 했었는데,
# 효율성에서 걸렸던 것으로 기억. 그래서 스택으로 풀라다가
# 스택으로 굳이 안 풀어도 되던 거로 기억...

def solution(s):
    tmp = 0

    for a in s:
        if tmp < 0: break
        
        if a == '(': tmp += 1
        else: tmp -= 1
            
    return tmp == 0