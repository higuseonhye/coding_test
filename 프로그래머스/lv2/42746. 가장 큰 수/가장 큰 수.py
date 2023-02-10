def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer

"""
주요 기능은 주어진 문자열들을 정렬하여 가장 큰 수를 만드는 것입니다. 
- 문자열들을 정렬할 때, key 매개변수를 사용하여 정렬하는 기준을 지정합니다. 
- 기준으로 x * 3을 사용하여, 각 문자열을 3번 반복한 것을 정렬 기준으로 사용합니다. 
- 정렬한 문자열들을 join 함수를 사용하여 모아서 int 타입으로 변환하여 정수로 변환하여 반환합니다.
"""
