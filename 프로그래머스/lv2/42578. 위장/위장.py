from collections import defaultdict
def solution(clothes):
    dic = defaultdict(int)
    for item, key in clothes:
        dic[key] += 1
    res = 1
    for key in dic.keys():
        res *= dic[key] + 1
    return res-1

