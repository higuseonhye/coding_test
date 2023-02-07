def solution(n, left, right):
    results = []
    for x in range(left, right+1):
        results.append(max(divmod(x, n)) + 1)
    return results

"""
이 코드는 주어진 n, left, right 값을 이용하여 1차원 배열을 만드는 solution 함수입니다.

results 빈 리스트를 생성합니다.
left와 right 값 사이의 모든 x 값에 대해서, x를 n으로 나눈 몫과 나머지를 구한 후, 그 중 가장 큰 값을 max() 함수를 이용하여 구합니다. 
구한 값에 1을 더한 후, results 리스트에 append() 함수를 이용하여 추가합니다.
results 리스트를 반환합니다.
"""
