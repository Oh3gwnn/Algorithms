def solution(a, b, c):
    for i in range(3):
        if (a != b) & (b != c) & (a != c):
            return a+b+c
        elif (a == b) & (b == c):
            return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
        else :
            return (a+b+c)*(a**2+b**2+c**2)