import sys
input = sys.stdin.readline

n = int(input())
Ltmp, Stmp = 0, 0
cnt = 0

for i in input()[:n]:
    if i == 'L' :
        Ltmp += 1
    elif i == 'S' :
        Stmp += 1

    elif i == 'R' :
        if Ltmp > 0 :
            cnt += 1
            Ltmp -= 1
        else : break
    
    elif i == 'K' :
        if Stmp > 0 :
            cnt += 1
            Stmp -= 1
        else : break
    else :
        cnt += 1

print(cnt)