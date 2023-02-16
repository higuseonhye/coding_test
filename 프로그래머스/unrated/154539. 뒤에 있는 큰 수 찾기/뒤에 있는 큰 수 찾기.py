def solution(numbers):
    answer = []
    stack = []
    for i, num in enumerate(numbers):
        while stack and stack[-1][1] < num:
            idx, val = stack.pop()
            answer[idx] = num
        stack.append((i, num))
        answer.append(-1)
    return answer

"""
우선, 빈 리스트인 answer와 스택인 stack을 초기화합니다. 
enumerate 함수를 이용하여 numbers 리스트를 인덱스와 함께 순회합니다. 
각각의 인덱스 i와 원소 num에 대해서, 스택이 비어있지 않고 스택의 맨 위에 있는 값이 현재 원소보다 작을 때까지 반복하여, 
    스택의 값을 꺼내면서 answer 리스트의 해당 인덱스에 현재 원소 num을 할당합니다. 
이후, 현재 원소의 인덱스와 값을 스택에 추가합니다. 
마지막으로, answer 리스트의 모든 값이 -1인 상태로 반환됩니다.
"""
