def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
        else:
            answer.append(len(prices)-i-1)
    return answer

"""
주어진 코드는 각 원소의 주식 가격 변화를 나타내는 리스트 prices의 각 원소를 기준으로, 그 값이 떨어지기 전에 같은 값이나 높은 값이 나오는 시간을 계산하는 함수이다.

예를 들어, prices가 [1, 2, 3, 2, 3]일 경우, 1이라는 값이 나오면 그 다음에 2가 나오므로 기준 값이 떨어지기 전에 2가 나온 것이다. 
따라서 결과 값에 1을 기준으로 하면 1의 위치에 1이 저장될 것이다.

내부 for 루프에서 값이 떨어지기 전에 같은 값이나 높은 값이 나올 때까지 반복한다. 
만약 마지막까지 값이 떨어지지 않았다면 (else 블록), 그 값은 전체 길이에서 현재 위치를 뺀 것이 기준 값이 떨어지기 전에 같은 값이나 높은 값이 나오지 않았음을 나타낸다.

마지막으로 결과 값인 리스트 answer를 반환한다.
"""
