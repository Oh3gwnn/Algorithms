# 생각은 비슷하게 했는데 str(int())를 안해서 자꾸 하나 통과 못했다.
# 보니까 [0,0,0,0]일 때 "0"이 나와야하는데 0000으로 나와서 그랬다.

# 그리고 간단한 람다는 사용하겠는데, 활용하려고 하면 조금 어려운 것 같다.
# 람다식 공부를 조금 더 해봐야겠다.

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))