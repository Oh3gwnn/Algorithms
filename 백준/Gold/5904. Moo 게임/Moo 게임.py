import sys
input = sys.stdin.readline

n= int(input())
moo_list = ['m', 'o', 'o']

def moo(n, k, prev):
    now_len = 2*prev + k + 3

    if n <= 3:
        print(moo_list[n-1])
        exit(0)
    
    if now_len < n: moo(n, k+1, now_len)
    else: 
        if n > prev and n <= (k + 3 + prev):
            if (n - prev) != 1: print('o')
            else: print('m')
            exit(0)
        else:
            moo(n-(prev + k + 3), 1, 3)

moo(n, 1, 3)