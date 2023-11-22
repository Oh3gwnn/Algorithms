import sys
input = sys.stdin.readline

s = input().upper().strip()
set_s = list(set(s))
ans = list()

for i in set_s:
    ans.append(s.count(i))
    
if ans.count(max(ans)) > 1: print("?")
else : print(set_s[ans.index(max(ans))])