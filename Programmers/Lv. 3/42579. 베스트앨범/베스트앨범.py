# 왠지 모르게 실패 하나때문에 못품
"""
def solution(genres, plays):
    answer = []
    genre_play = {}
    play_dic = {}
    genre_max = {}
    
    # 고유번호별 재생 횟수 딕셔너리
    for i in range(len(plays)):
        play_dic[plays[i]] = i
        
    # 장르별 고유번호, 많이 재생된 장르 딕셔너리
    for i in range(len(genres)):
        if genres[i] in genre_play:
            genre_play[genres[i]] += [plays[i]]
            genre_max[genres[i]] += plays[i]
        else:
            genre_play[genres[i]] = [plays[i]]
            genre_max[genres[i]] = plays[i]
            
    # 가장 많이 재생된 노래 두 곡
    for i in genre_play:
        if len(genre_play[i]) >= 2:
            genre_play[i] = sorted(genre_play[i], reverse = True)[0:2]
            
    #많이 재생된 장르 내림차순 정리
    genre_max = dict(sorted(genre_max.items(), key = lambda x:x[1] ,reverse = True))
    
    #return
    for i in genre_max:
        for j in genre_play[i]:
            answer.append(play_dic[j])
    
    return answer
"""

# 안되서 그냥 처음부터 다시 자꾸 두개만 안된다 왤까?
"""
def solution(genres, plays):
    answer = []
    genre_play = {}
    play_dic = {}
    genre_max = {}
    
    # 재생횟수 : 고유번호
    for i in range(len(plays)):
        if plays[i] in play_dic:
            play_dic[plays[i]] += i
        else:
            play_dic[plays[i]] = i
            
    # 장르 : 재생 횟수
    # 많이 재생된 장르 딕셔너리
    for i in range(len(genres)):
        if genres[i] in genre_play:
            genre_play[genres[i]] += [plays[i]]
            genre_max[genres[i]] += plays[i]
        else:
            genre_play[genres[i]] = [plays[i]]
            genre_max[genres[i]] = plays[i]
    
    #1 가장 많이 재생된 장르 내림차순 정리
    genre_max = dict(sorted(genre_max.items(), key = lambda x:x[1] ,reverse = True))
    
    #2 장르별 가장 많이 재생된 노래 내림차순 정리
    for i in genre_play:
        if len(genre_play[i]) >= 2:
            genre_play[i] = sorted(genre_play[i], reverse = True)[0:2]

    #3 결과 도출
    for i in genre_play.values():
        for j in range(len(i)):
            i[j] = play_dic.get(i[j])
            
    for i in genre_max:
        for j in genre_play[i]:
            answer.append(j)

    return answer
"""
# 결국 참고...
def solution(genres, plays):
    answer = []
    
    gip = {}
    genSum = {}
    inum = {}
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in gip:
            gip[g] = [(i, p)]
        else:
            gip[g].append((i, p))

        if g not in genSum:
            genSum[g] = p
        else:
            genSum[g] += p
                
    for (k, v) in sorted(genSum.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(gip[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    
    return answer