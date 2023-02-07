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

"""
이 코드는 두 개의 문자열 str1 과 str2의 유사도를 계산하는 프로그램입니다. 
유사도 계산은 두 문자열에 포함된 2글자 짧은 단어(서로 대소문자 구분 없음)의 교집합(intersection)과 합집합(union)의 비율로 계산합니다.

첫째, 두 문자열을 2글자씩 끊어서 딕셔너리 형태로 변환하는 getDict 함수를 사용합니다. 
그리고 각 딕셔너리의 key 값만을 집합 형태로 변환하여 set1과 set2로 저장합니다.

둘째, 교집합과 합집합을 구하는 getIntersectionCount 함수와 getUnionCount 함수를 사용합니다. 
이 두 함수에서는 각각 교집합의 크기와 합집합의 크기를 구하며, 교집합 크기를 합집합 크기로 나눈 것이 두 문자열의 유사도입니다.

셋째, 유사도 계산 결과는 65536으로 나누어서 정수로 변환합니다.

마지막으로, 계산된 answer를 반환합니다.
"""

"""
이 코드는 두 개의 문자열을 입력받아 두 문자열에서 공통적으로 사용된 문자쌍(2-gram)의 Jaccard similarity index를 구하는 프로그램입니다.

두 개의 문자열을 입력받아 solution 함수를 실행합니다.
각 문자열을 get_dict 함수를 통해 문자쌍의 빈도수를 가지는 딕셔너리 형태로 변환합니다.
두 개의 딕셔너리에서 공통적으로 등장하는 문자쌍을 찾아 교집합(inter_num)의 개수를 구합니다.
두 개의 딕셔너리에 등장하는 모든 문자쌍을 합친 것(합집합, union_num)을 구합니다.
교집합 개수를 합집합 개수로 나눈 것이 Jaccard similarity index이며, 이를 65536으로 곱한 결과를 answer에 저장합니다.
answer를 반환합니다.
"""

"""
This is a Python3 code that calculates the Jaccard index between two strings str1 and str2.

The Jaccard index is a similarity measure between sets and is defined as the size of the intersection divided by the size of the union of the two sets.

The code first imports the re library and defines a function solution that takes two input strings str1 and str2. 
It then calls the get_dict function on both str1 and str2 to generate dictionaries of all unique two-letter substrings from each string, along with their frequency.

The sets of these substrings are then formed by calling set on the dictionaries, and the intersection and union of the sets are computed. 
The number of elements in the intersection and union are then used to compute the Jaccard index.

Finally, the Jaccard index is multiplied by 65536 and rounded down to the nearest integer. The result is returned as the final answer.

The get_dict function uses a regular expression to match all two-letter substrings and a dictionary to store each substring along with its frequency. 
The function then returns this dictionary.
"""
