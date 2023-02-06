import numpy as np

def solution(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    return (arr1 @ arr2).tolist()

"""
첫 번째 줄에서 numpy 라이브러리를 import 합니다.
solution 함수에서 arr1과 arr2를 numpy 배열로 변환합니다.
arr1 @ arr2는 행렬 곱셈을 수행하는 표현입니다.
.tolist() 메소드를 사용하여 곱셈 결과를 파이썬 리스트로 변환하여 반환합니다.
"""

def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

"""
answer 리스트를 len(arr1) 행 len(arr2[0]) 열로 생성하여 초기화합니다.
첫 번째 for문에서는 arr1의 행을 순회합니다.
두 번째 for문에서는 arr2의 열을 순회합니다.
세 번째 for문에서는 arr2의 행을 순회하며, arr1의 i행과 arr2의 k행을 곱하여 결과를 answer[i][j]에 누적합니다.
최종적으로 answer 리스트를 반환합니다.
"""
