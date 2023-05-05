import sys
input = sys.stdin.readline

while True: 
    s = str(input().rstrip())
    if s == "0": break
    else: print("yes" if s == s[-1::-1] else "no")