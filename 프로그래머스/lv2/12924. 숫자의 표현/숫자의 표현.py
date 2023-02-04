"""
for i in range(1, (n//2)+1)에서 n//2+1의 값은 첫 번째 루프에서 검사하는 숫자의 범위를 제한합니다.
그리고 for j in range(i, n)에서 j는 현재 루프에서 검사하는 연속된 자연수입니다. 
루프 내에서는 연속된 자연수의 합 sum을 계속 구하며 sum == n이 되면 표현의 방법의 수를 증가시킵니다. 
sum > n이 되면 검사할 필요 없이 루프를 빠져나옵니다.
마지막으로 answer += 1은 n = n인 경우를 고려합니다.
최종 결과는 answer로 반환됩니다.
"""

def solution(n): #15
    answer = 0 
    for i in range(1, (n//2)+1): 
        sum = 0
        for j in range(i, n): 
            sum += j 
            if sum == n:
                answer += 1
                break
            if sum > n:
                break
    answer += 1
    return answer
