from collections import defaultdict

def solution(clothes):
    dic = defaultdict(int)
    for item, key in clothes:
        dic[key] += 1
    res = 1
    for key in dic.keys():
        res *= dic[key] + 1
    return res-1

"""
이 코드는 옷의 종류(item)와 카테고리(key)를 입력으로 받아 옷을 입을 수 있는 모든 조합의 개수를 계산하는 함수입니다.

defaultdict(int) 는 딕셔너리의 기본 값을 0으로 설정한 것으로, 새로운 키에 대한 값이 없을 경우 기본값으로 0이 사용됩니다.

dic이라는 딕셔너리에서 key 값을 기준으로 옷의 종류가 있는지 확인하고 있으며, 있을 경우 해당 키의 값을 1 증가시킵니다.

그 후, res 라는 변수를 1로 초기화하고, 딕셔너리의 키 개수만큼 반복문을 수행하여 각 키에 대한 옷 개수에 1을 더한 값을 곱하여 res에 저장합니다.

마지막으로 res-1을 반환하여, 아무것도 안 입는 경우를 제외한 결과값을 반환합니다.
"""
