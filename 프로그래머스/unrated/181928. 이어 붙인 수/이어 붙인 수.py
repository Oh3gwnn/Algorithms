def solution(num_list):
    odd, even = [], []
    for i in num_list:
        if i%2==1: odd += str(i)
        else: even += str(i)
    return int("".join(odd))+int("".join(even))