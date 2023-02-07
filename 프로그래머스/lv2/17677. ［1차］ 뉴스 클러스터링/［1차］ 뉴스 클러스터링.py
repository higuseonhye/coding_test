import re

def solution(str1, str2):
    answer = 0
    data1 = get_dict(str1)
    data2 = get_dict(str2)

    set1 = set(data1)
    set2 = set(data2)

    inter_num = sum(min(data1.get(i, 0), data2.get(i, 0)) for i in set1 & set2)
    union_num = sum(max(data1.get(i, 0), data2.get(i, 0)) for i in set1 | set2)

    if union_num == 0:
        res = 1
    else:
        res = inter_num / union_num

    answer = int(res * 65536)
    return answer

def get_dict(sten):
    p = re.compile(r'[a-zA-Z]{2}')
    data = {}
    for i in range(len(sten) - 1):
        if p.match(sten[i:i + 2]):
            key = (sten[i:i + 2]).lower()
            data[key] = data.setdefault(key, 0) + 1

    return data
