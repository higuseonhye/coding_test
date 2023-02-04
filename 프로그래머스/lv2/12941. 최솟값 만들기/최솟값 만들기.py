"""
A, B 배열을 각각 오름차순, 내림차순으로 정렬합니다.
A, B 배열을 각각 하나씩 뽑아 곱한 값을 sum 함수에 누적합니다.
누적된 값을 리턴합니다.
"""
def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    return sum(a*b for a,b in zip(A,B))

"""
zip: https://wikidocs.net/32#zip
map: https://codechacha.com/ko/python-join-lists/
"""
