def solution(genres, plays):
    dic = {}
    for i, genre in enumerate(genres):
        if genre in dic:
            dic[genre].append((i, plays[i]))
        else:
            dic[genre] = [(i, plays[i])]
    dic = {k: sorted(v, key=lambda x: x[1], reverse=True) for k, v in dic.items()}
    dic = sorted(dic.items(), key=lambda x: sum(map(lambda y: y[1], x[1])), reverse=True)
    answer = []
    for _, lst in dic:
        for i in range(min(len(lst), 2)):
            answer.append(lst[i][0])
    return answer
