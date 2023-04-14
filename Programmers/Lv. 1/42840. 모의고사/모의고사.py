# 사람들은 생각보다 더 줄여서 풀어버린다. 그래서 if문을 저렇게 썼다.
# 한눈에 이해라도 잘되니 상관없나...모르겠다.
def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]
    oneans, twoans, thrans = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == one[i%5]: oneans += 1
        if answers[i] == two[i%8]: twoans += 1
        if answers[i] == thr[i%10]: thrans += 1

    tmp = max(oneans, twoans, thrans)
    if tmp == oneans: answer.append(1)
    if tmp == twoans: answer.append(2)
    if tmp == thrans: answer.append(3)
    return answer