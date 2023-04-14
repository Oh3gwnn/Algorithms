# 가로 세로 최댓값 중 하나만 바꾸는 걸로 했다가 안되서
# 두 수를 비교하고 큰 수가 가로로만 오게끔 하고 다시했다.

def solution(sizes):
    answer = 0
    i = 0
    width = []
    height = []
    
    for w, h in sizes:
        if h > w:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        i += 1
    
    for w, h in sizes:
        width.append(w)
        height.append(h)
    
    answer = max(width) * max(height)
    
    return answer