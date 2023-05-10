import sys
input = sys.stdin.readline

# 예상은 했는데 역시 시간초과
# def fibonacci(x):
#     global zero
#     global one

#     if x == 0:
#         zero += 1
#         return 0
#     elif x == 1:
#         one += 1
#         return 1
#     else:
#         return fibonacci(x-1) + fibonacci(x-2)
        
# n = int(input())

# for _ in range(n):
#     zero, one = 0, 0
#     fibonacci(int(input()))
#     print(zero, one)

# 사람들은 피보나치의 0과 1의 규칙을 이용하였다.
n = int(input())

for _ in range(n):
    zero, one = [1, 0], [0, 1]
    
    x = int(input())

    if x > 1:
        for i in range(x - 1):
            zero.append(one[-1])
            one.append(zero[-2] + one[-1])

    print(zero[x], one[x])